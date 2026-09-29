FROM python:3.14

RUN apt update && export DEBIAN_FRONTEND=noninteractive

RUN apt install lsb-release 

WORKDIR /workspaces/imparare-surface-materdei-neo/

COPY /requirements.txt /tmp
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/requirements.txt \
  && rm /tmp/requirements.txt

COPY ImpararePackage /workspaces/imparare-surface-materdei-neo/ImpararePackage
COPY setup.py /workspaces/imparare-surface-materdei-neo

# Install the custom module using pip
RUN pip install .

COPY . /workspaces/imparare-surface-materdei-neo/ScriptsLibrary

CMD ["tail", "-f", "/dev/null"]