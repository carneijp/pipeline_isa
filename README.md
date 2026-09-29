# Imparare Surface

Repositório dedicado ao desenvolvimento e manutenção do processo de ETL da Quali, em Python.

## Teste local

Para testar o processo localmente, recomenda-se construir a imagem Docker padronizada e executá-la em um container:

```{ sh }
# Constrói imagem Docker
docker build -t imparare-surface-service .

# Executa container
docker run -d --name imparare-surface-service imparare-surface-service
```

## Deployment

Para realizar deployment de uma nova versão do serviço, deve-se:

1. Realizar login no ECR da Qualis
  - Utilizar comando `aws configure` para configurar as chaves AWS relativas ao ECR
  - Utilizar o seguinte comando para realizar login via Docker no ECR: `aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin 933069487772.dkr.ecr.sa-east-1.amazonaws.com`
2. Realizar build da imagem utilizando a tag padronizada que aponta ao ECR da Qualis (mudando a `VERSÃO` sempre, conforme o [padrão de versionamento semântico](https://semver.org/spec/v2.0.0-rc.2.html)): ```docker build -t 933069487772.dkr.ecr.sa-east-1.amazonaws.com/imparare-surface-service:{ VERSÃO } .```
  1. É recomendado que se realize testes sobre esta imagem, executando-a em um container local como indicado na seção anterior
3. Enviar imagem construída ao ECR da Qualis: `docker push 933069487772.dkr.ecr.sa-east-1.amazonaws.com/imparare-surface-service:{ VERSÃO }`
4. Avisar equipe da Nuvme para atualizarem o cronjob no Kubernetes, apontando-o para esta nova versão da imagem e realizado quaisquer alterações necessárias nos Secrets (variáveis de ambiente)

## Execução manual do cronjob em Kubernetes

- Acessar o [Rancher da Qualis](https://rancher.portalqualis.com.br/) e realizar login 
- Acessar `Workload -> CronJobs` pela sidebar da esquerda
- Acessar o cronjob específico do processo de ETL
- Acessar o menu de `...` à direita e clicar em `Run Now`


## Criaçao de tabelas no banco da cloud pro microservice:
-- Create elk_indexes
CREATE TABLE public.elk_indexes (
	id text NOT NULL,
	"key" text NOT NULL,
	value text NOT NULL,
	company_id uuid NULL,
	CONSTRAINT "UQ_9dfc66630a611662b49ecf9ef47" UNIQUE (id)
);

-- ===============================================================================================================================================

-- Create isa_avaliacao
CREATE TABLE public.isa_avaliacao (
	id text NOT NULL,
	paciente_id int8 NULL,
	dt_infeccao timestamptz NULL,
	tipo_infeccao text NULL,
	avaliacao_status text NULL,
	avaliacao_data text NULL,
	avaliacao_responsavel text NULL,
	avaliacao_comentario text NULL,
	notificado text NULL,
	comunitaria bool NULL,
	local_infeccao text NULL,
	aval_dt_infec timestamptz NULL,
	relacionado bool NULL,
	outra_infec text NULL,
	suspeita_id text NULL,
	suspeita_payload text NULL,
	obito_relacionado_a_infeccao varchar(20) NULL,
	relacionado_cateter_sonda bool NULL,
	potencial_contaminacao varchar(250) NULL,
	classificacao_infeccao varchar(250) NULL,
	microorganismo_id int4 NULL,
	company_id uuid NULL,
	CONSTRAINT "ISA_avaliacao_pkey" PRIMARY KEY (id)
);
CREATE INDEX avaliacao_idx ON public.isa_avaliacao USING btree (paciente_id);
CREATE INDEX avaliacao_idx2 ON public.isa_avaliacao USING btree (dt_infeccao);
CREATE INDEX idx_avaliacao_pacientes ON public.isa_avaliacao USING btree (paciente_id, outra_infec);
CREATE INDEX idx_fk_avaliacao_paciente ON public.isa_avaliacao USING btree (paciente_id);
CREATE INDEX idx_pk_avaliacao ON public.isa_avaliacao USING btree (id);

-- ===============================================================================================================================================

-- Create isa_microorganismos
CREATE SEQUENCE public.isa_microrganismos_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

CREATE TABLE public.isa_microorganismos (
	id int4 NOT NULL DEFAULT nextval('isa_microrganismos_id_seq'::regclass),
	nome varchar(250) NULL,
	company_id uuid NULL,
	CONSTRAINT isa_microrganismos_pk PRIMARY KEY (id)
);

-- ===============================================================================================================================================

-- Create isa_avaliacao_microorganismos
CREATE SEQUENCE public.isa_avaliacao_microorganismos_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

CREATE TABLE public.isa_avaliacao_microorganismos (
	id serial4 NOT NULL,
	avaliacao_id text NOT NULL,
	microorganismo_id int4 NOT NULL,
	resistente text NULL,
	company_id uuid NULL,
	CONSTRAINT isa_avaliacao_microorganismos_pkey PRIMARY KEY (id)
);


-- public.isa_avaliacao_microorganismos foreign keys
ALTER TABLE public.isa_avaliacao_microorganismos ADD CONSTRAINT fk_avaliacao FOREIGN KEY (avaliacao_id) REFERENCES public.isa_avaliacao(id);
ALTER TABLE public.isa_avaliacao_microorganismos ADD CONSTRAINT fk_microorganismo FOREIGN KEY (microorganismo_id) REFERENCES public.isa_microorganismos(id);

-- ===============================================================================================================================================

-- Create isa_centro_fato
CREATE TABLE public.isa_centro_fato (
	id int8 NULL,
	fato_tipo text NULL,
	paciente_id int8 NULL,
	exame_id text NULL,
	sinais_id text NULL,
	procedimento_id text NULL,
	medicamento_id text NULL,
	laudo_id text NULL,
	encontro_id text NULL,
	evidencia_id text NULL,
	infeccao_id text NULL,
	suspeita_id text NULL,
	dthr_fato timestamp NULL,
	company_code text NULL,
	company_id text NULL
);
CREATE INDEX centro_fato_idx ON public.isa_centro_fato USING btree (suspeita_id);
CREATE INDEX centro_fato_idx2 ON public.isa_centro_fato USING btree (infeccao_id);

-- ===============================================================================================================================================

-- Create isa_companies
CREATE TABLE public.isa_companies (
	id uuid NOT NULL,
	"name" text NOT NULL,
	code text NOT NULL,
	sso_client_name text NOT NULL,
	CONSTRAINT "PK_4711c1cc17e9492ba4b6a5f280a" PRIMARY KEY (id),
	CONSTRAINT "UQ_216a287f5e0ca4ded72e74a294f" UNIQUE (name),
	CONSTRAINT "UQ_a97de9a20d452dd0f458e7e4c36" UNIQUE (sso_client_name),
	CONSTRAINT "UQ_d52e9703f3783524297917ec90c" UNIQUE (code)
);

-- ===============================================================================================================================================

-- Create isa_configuracao
CREATE TABLE public.isa_configuracao (
	id text NULL,
	meta text NULL,
	value text NULL,
	created_at text NULL,
	updated_at text NULL,
	user_id text NULL
);

-- ===============================================================================================================================================

-- Create isa_encontro
CREATE TABLE public.isa_encontro (
	id text NULL,
	prontuario int8 NULL,
	dt_encontro timestamp NULL,
	local_encontro text NULL,
	termos_texto text NULL,
	texto_evolucao_agg text NULL,
	fst_evo_medica text NULL,
	fst_termos_texto_medico text NULL,
	termos_achados text NULL,
	company_code text NULL,
	company_id text NULL,
	criterios_extraidos text NULL
);

-- ===============================================================================================================================================

-- Create isa_encontro_joined_prepared
CREATE TABLE public.isa_encontro_joined_prepared (
	id text NULL,
	prontuario int8 NULL,
	dt_encontro timestamp NULL,
	local_encontro text NULL,
	termos_texto text NULL,
	texto_evolucao_agg text NULL,
	fst_evo_medica text NULL,
	fst_termos_texto_medico text NULL,
	termos_achados text NULL
);

-- ===============================================================================================================================================

-- Create isa_exame
CREATE TABLE public.isa_exame (
	id text NULL,
	patient_id int8 NULL,
	exame text NULL,
	item_exame text NULL,
	dthr_pedido timestamp NULL,
	dthr_entrega timestamp NULL,
	resultado text NULL,
	tipo_atendimento text NULL,
	ordem_amostra text NULL,
	data_assinatura timestamp NULL,
	ordem text NULL,
	criterio text NULL,
	gmr text NULL,
	company_code text NULL,
	company_id text NULL,
	positivo text NULL,
	pcr_covid text NULL
);

-- ===============================================================================================================================================

-- Create isa_infeccao
CREATE TABLE public.isa_infeccao (
	id text NULL,
	paciente_id int8 NULL,
	dt_infeccao timestamp NULL,
	prob_perc float8 NULL,
	prob_perc_pnm float8 NULL,
	pred_pnm float8 NULL,
	prob_perc_traqueo float8 NULL,
	pred_traqueo float8 NULL,
	prob_perc_pav float8 NULL,
	pred_pav float8 NULL,
	prob_perc_itu float8 NULL,
	pred_itu float8 NULL,
	prob_perc_isc float8 NULL,
	pred_isc float8 NULL,
	prob_perc_ipcs float8 NULL,
	pred_ipcs float8 NULL,
	dt_inicio timestamp NULL,
	dt_fim timestamp NULL,
	company_code text NULL,
	company_id text NULL
);
CREATE INDEX infeccao_idx ON public.isa_infeccao USING btree (id);
CREATE INDEX infeccao_idx2 ON public.isa_infeccao USING btree (paciente_id);
CREATE INDEX infeccao_idx3 ON public.isa_infeccao USING btree (dt_infeccao);
CREATE INDEX infeccao_idx4 ON public.isa_infeccao USING btree (prob_perc);

-- ===============================================================================================================================================

-- Create isa_internacoes
CREATE TABLE public.isa_internacoes (
	paciente_id int8 NULL,
	cd_atendimento int8 NULL,
	dthr_atendimento timestamp NULL,
	dthr_alta timestamp NULL,
	tipo_alta text NULL,
	tempo_estadia int8 NULL,
	company_code text NULL,
	company_id text NULL
);

-- ===============================================================================================================================================

-- Create isa_laudo
CREATE TABLE public.isa_laudo (
	id text NULL,
	patient_id int8 NULL,
	codigo_laudo int8 NULL,
	descricao_laudo text NULL,
	dthr_pedido timestamp NULL,
	dthr_entrega_laudo timestamp NULL,
	laudo_texto text NULL,
	tipo_atendimento text NULL,
	ordem text NULL,
	criterio text NULL,
	company_code text NULL,
	company_id text NULL
);

-- ===============================================================================================================================================

-- Create isa_logs
CREATE TABLE public.isa_logs (
	id serial4 NOT NULL,
	chave varchar(1000) NOT NULL,
	valor varchar(250) NULL,
	created_at timestamp NOT NULL DEFAULT now(),
	CONSTRAINT "PK_3dfa54dee4a8bdb9383ce3befc3" PRIMARY KEY (id)
);

-- ===============================================================================================================================================

-- Create isa_medicamento
CREATE TABLE public.isa_medicamento (
	id text NULL,
	patient_id int8 NULL,
	codigo_prescricao int8 NULL,
	dthr_prescricao timestamp NULL,
	medicamento text NULL,
	dose text NULL,
	unidade text NULL,
	frequencia text NULL,
	via text NULL,
	tipo_atendimento text NULL,
	ordem text NULL,
	criterio text NULL,
	company_code text NULL,
	company_id text NULL
);

-- ===============================================================================================================================================

-- Create isa_pacientes
CREATE TABLE public.isa_pacientes (
	id int8 NULL,
	sexo text NULL,
	dt_nascimento timestamp NULL,
	idade_hoje int8 NULL,
	nome text NULL,
	company_code text NULL,
	company_id text NULL
);
CREATE INDEX paciente_idx ON public.isa_pacientes USING btree (id);
CREATE INDEX paciente_idx2 ON public.isa_pacientes USING btree (nome);

-- ===============================================================================================================================================

-- Create isa_pacientes_comentarios
CREATE TABLE public.isa_pacientes_comentarios (
	id serial4 NOT NULL,
	feito_por varchar NULL,
	comentario text NULL,
	criado_em timestamp NOT NULL DEFAULT now(),
	atualizado_em timestamp NOT NULL DEFAULT now(),
	deletado_em timestamp NULL,
	paciente_id int4 NULL,
	company_id uuid NULL,
	CONSTRAINT "PK_14b8190a59589fb3aff568d5a3b" PRIMARY KEY (id)
);

-- ===============================================================================================================================================

-- Create isa_pacientes_joined
CREATE TABLE public.isa_pacientes_joined (
	"REGISTRO" int8 NULL,
	"SEXO" text NULL,
	"DT_NASCIMENTO_parsed" timestamp NULL,
	"Idade Hoje" int8 NULL,
	nome text NULL
);

-- ===============================================================================================================================================

-- Create isa_procedimento
CREATE TABLE public.isa_procedimento (
	id text NULL,
	perfil text NULL,
	prestador int8 NULL,
	patient_id int8 NULL,
	dthr_criacao timestamp NULL,
	dthr_procedimento timestamp NULL,
	dthr_fim_procedimento timestamp NULL,
	tempo_cirurgia float8 NULL,
	texto_cirurgia text NULL,
	nome_medico text NULL,
	nome_procedimentos text NULL,
	tipo_atendimento text NULL,
	ordem text NULL,
	criterio text NULL,
	company_code text NULL,
	company_id text NULL
);

-- ===============================================================================================================================================

-- Create isa_relatorio
CREATE TABLE public.isa_relatorio (
	"key" text NULL,
	um_mes text NULL,
	tres_meses text NULL,
	seis_meses text NULL,
	doze_meses text NULL,
	tudo text NULL,
	company_id text NULL
);

-- ===============================================================================================================================================

-- Create isa_sinal_vital
CREATE TABLE public.isa_sinal_vital (
	id text NULL,
	paciente_id int8 NULL,
	tipo_sinal text NULL,
	dthr_coleta timestamp NULL,
	valor text NULL,
	unimedida text NULL,
	perfil text NULL,
	tipo_atendimento text NULL,
	ordem text NULL,
	criterio text NULL,
	company_code text NULL,
	company_id text NULL
); 

-- ===============================================================================================================================================

-- Create isa_status
CREATE TABLE public.isa_status (
	id text NULL,
	contexto text NULL,
	status text NULL,
	company_id uuid NULL
);

-- ===============================================================================================================================================

-- Create isa_suspeita
CREATE TABLE public.isa_suspeita (
	id text NULL,
	paciente_id int8 NULL,
	cd_atendimento int8 NULL,
	dthr_alta timestamp NULL,
	dt_infeccao timestamp NULL,
	prob_perc float8 NULL,
	max_prob float8 NULL,
	criterio text NULL,
	dthr_internacao timestamp NULL,
	company_code text NULL,
	company_id text NULL
);
CREATE INDEX suspeita_paciente_idx ON public.isa_suspeita USING btree (id);
CREATE INDEX suspeita_paciente_idx2 ON public.isa_suspeita USING btree (paciente_id);
CREATE INDEX suspeita_paciente_idx3 ON public.isa_suspeita USING btree (dt_infeccao);
CREATE INDEX suspeita_paciente_idx4 ON public.isa_suspeita USING btree (prob_perc);
CREATE INDEX suspeita_paciente_idx5 ON public.isa_suspeita USING btree (max_prob);

-- ===============================================================================================================================================

-- Create isa_suspeita_perc 
CREATE TABLE public.isa_suspeita_perc (
	max_prob float8 NULL,
	paciente_id int8 NULL,
	dt_infeccao timestamp NULL
);
CREATE INDEX isa_suspeita_perc_idx ON public.isa_suspeita_perc USING btree (paciente_id, dt_infeccao);
CREATE INDEX suspeita_perc_idx ON public.isa_suspeita_perc USING btree (paciente_id);
CREATE INDEX suspeita_perc_idx2 ON public.isa_suspeita_perc USING btree (dt_infeccao);
CREATE INDEX suspeita_perc_idx3 ON public.isa_suspeita_perc USING btree (max_prob);

-- ===============================================================================================================================================

-- Create isa_suspeita_v2_prepared
CREATE TABLE public.isa_suspeita_v2_prepared (
	id text NULL,
	paciente_id int8 NULL,
	cd_atendimento int8 NULL,
	dthr_alta timestamp NULL,
	dt_infeccao date NULL,
	prob_perc float8 NULL,
	max_prob float8 NULL,
	criterio text NULL,
	dthr_internacao timestamp NULL
);

-- ===============================================================================================================================================

-- Create isa_unidades
CREATE TABLE public.isa_unidades (
	id int8 NULL,
	unidades text NULL,
	company_id uuid NULL
);

-- ===============================================================================================================================================

-- Create migrations
CREATE TABLE public.migrations (
	id serial4 NOT NULL,
	"timestamp" int8 NOT NULL,
	"name" varchar NOT NULL,
	CONSTRAINT "PK_8c82d7f526340ab734260ea46be" PRIMARY KEY (id)
);

-- ===============================================================================================================================================

-- Create typeorm_metadata
CREATE TABLE public.typeorm_metadata (
	"type" varchar NOT NULL,
	"database" varchar NULL,
	"schema" varchar NULL,
	"table" varchar NULL,
	"name" varchar NULL,
	value text NULL
);