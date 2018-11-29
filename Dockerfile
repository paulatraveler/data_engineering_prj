FROM rocker/r-base:latest

MAINTAINER Paula Kmicinska <p.kmicinska@gmail.com>


# INSTALL PYTHON
RUN apt-get update \
    && apt-get install -y python3.6 \
    && apt-get install -y python3-pip

# INSTALL PROJECT-SPECIFIC DEPENDENCIES
COPY . /vente-privee
RUN pip3 install -r vente-privee/requirements.txt && cd vente-privee && pip3 install -e .

WORKDIR vente-privee

# RUN APPLICATION
RUN python3.6 vente_privee/app.py