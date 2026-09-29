import sqlalchemy as sa
import os
import pandas as pd
from io import StringIO
import csv
import numpy as np
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from elasticsearch import Elasticsearch
from sqlalchemy.pool import NullPool

chunckPadrao = 2000


ELASTICSEARCH_LOGIN = "elastic"
ELASTICSEARCH_PASSWORD = "Qu@lis2006*"
ELASTICSEARCH_URL = "https://elasticsearch.roboisa.com.br/"
ELASTICSEARCH_CONNECTION = Elasticsearch(hosts= ELASTICSEARCH_URL, basic_auth= (ELASTICSEARCH_LOGIN, ELASTICSEARCH_PASSWORD), request_timeout=300)

REMOTELOGIN = "materdei_neo"
REMOTEPASSOWORD = "c>37Pi3,p_8*"
REMOTEHOST = "roboisa-prd.cq4frpe2fx4i.sa-east-1.rds.amazonaws.com"
REMOTEDATABASE_NAME = "materdei_neo_prd"

REMOTEDATABASE = sa.create_engine(
    f"postgresql+psycopg2://{REMOTELOGIN}:{REMOTEPASSOWORD}@{REMOTEHOST}/{REMOTEDATABASE_NAME}",
    insertmanyvalues_page_size = 10000,
    pool_pre_ping = True, 
    pool_timeout = 3600, 
    pool_size = 0,
    #echo_pool = 'debug',
    max_overflow = 0,
    pool_recycle = 20
)


DATABASE_USER = 'materdei_neo'
DATABASE_PASSWORD = 'teste123'
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 5433
DATABASE_NAME = 'dbmaterdei_neo'

DATABASE_URL = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

LOCALDATABSE = sa.create_engine(
    DATABASE_URL,
    insertmanyvalues_page_size=10000,
    poolclass=NullPool,
    pool_pre_ping=True
)

WELLHEAD_USER = "wellhead-materdei-prod"
WELLHEAD_PASSWORD = "+WFI}hGP]aOs=3I%"
WELLHEAD_HOST = "db-wellhead-service-prod.portalqualis.com.br"
WELLHEAD_NAME = "wellhead-materdei-prd"

WELLHEAD_URL = f"postgresql+psycopg2://{WELLHEAD_USER}:{WELLHEAD_PASSWORD}@{WELLHEAD_HOST}/{WELLHEAD_NAME}"

ENGINEWELLHEAD = sa.create_engine(
    WELLHEAD_URL,
    pool_pre_ping = True, 
    pool_timeout = 3600,
    pool_size = 0,
    #echo_pool = 'debug',
    max_overflow = 0,
    pool_recycle = 20
)

# Real Batching: https://pythonspeed.com/articles/pandas-sql-chunking/
def get_data(queryText:str, isWellheadEngine: bool = False, isLocal: bool = True, chunck:int = chunckPadrao):
    query = sa.text(queryText)
    if isWellheadEngine:
        #with engineWELLHEAD.connect() as connection:
            #connection.begin()
        if chunck != None:
            conn = ENGINEWELLHEAD.execution_options(stream_results=True)
            df = pd.read_sql(query, conn, index_col= None, chunksize= chunck)
        else:
            df = pd.read_sql(query, ENGINEWELLHEAD, index_col= None)
            #connection.commit()
    else :
        #with dataBaseSource.connect() as connection:
        #    connection.begin()
        dataBaseSource = LOCALDATABSE.execution_options(stream_results=True) if isLocal else REMOTEDATABASE.execution_options(stream_results=True)
        if chunck != None:
            df = pd.read_sql(query, dataBaseSource, index_col= None, chunksize= chunck)
        else:
            df = pd.read_sql(query, dataBaseSource, index_col= None)
        #    connection.commit()

    return df

# reajustar o padrao do if_exists caso seja script diario, ou caso seja treinamento, caso de treinmento utilizar replace e caso de diario append
# trocar o nome da varia if_existes para rotina
# OBS: Handling Pessimistic Connection - https://docs.sqlalchemy.org/en/20/core/pooling.html#disconnect-handling-pessimistic
def set_data_on_sql(df: pd.DataFrame, nomeTabelaDestino: str, schema: str= "public", if_exists:str = "replace", engine: sa.Engine = None, isLocal: bool = True):

    engine = (LOCALDATABSE if isLocal else REMOTEDATABASE) if engine is None else engine
    
    if if_exists == 'replace':
        df.to_sql(nomeTabelaDestino, schema= schema, con= engine, if_exists= if_exists, index= False, method= 'multi')
    else:
        df.to_sql(nomeTabelaDestino, schema= schema, con= engine, if_exists= if_exists, index= False, method= psql_insert_copy)


def psql_insert_copy(table, conn, keys, data_iter):
    """
    Execute SQL statement inserting data

    Parameters
    ----------
    table : pandas.io.sql.SQLTable
    conn : sqlalchemy.engine.Engine or sqlalchemy.engine.Connection
    keys : list of str
        Column names
    data_iter : Iterable that iterates the values to be inserted
    """
    # gets a DBAPI connection that can provide a cursor
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join(['"{}"'.format(k) for k in keys])
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name

        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
            table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)


# o comando _execute_ deve permitir a execução de comandos em uma database PostgreSQL, 
#  como por exemplo a criação de INDEX para as tabelas
# https://docs.sqlalchemy.org/en/20/core/connections.html
def execute(queryText:str, schema: str= "public", isWellheadEngine: bool = False, isLocal: bool = True): #engine:sa.Engine = dataBaseSource):
    if isWellheadEngine:
        with ENGINEWELLHEAD.connect() as connection:
            connection.execute(sa.text(queryText))
            connection.commit()
    else :
        engine = LOCALDATABSE if isLocal else REMOTEDATABASE
        with engine.connect() as connection:
                connection.execute(sa.text(queryText))
                connection.commit()
