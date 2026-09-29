FROM python:3.14

RUN apt update && export DEBIAN_FRONTEND=noninteractive

RUN apt install lsb-release 

WORKDIR /workspaces/pipeline_isa/

COPY /requirements.txt /tmp
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt \
  && rm /tmp/requirements.txt

COPY ImpararePackage /workspaces/pipeline_isa/ImpararePackage
COPY setup.py /workspaces/pipeline_isa

# Install the custom module using pip
RUN pip install .

COPY . /workspaces/pipeline_isa/ScriptsLibrary

CMD ["tail", "-f", "/dev/null"]