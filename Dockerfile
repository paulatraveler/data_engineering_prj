FROM rocker/r-base:latest

MAINTAINER Paula Kmicinska <p.kmicinska@gmail.com>


# INSTALL PYTHON
RUN apt-get update \
    && apt-get install -y python3.6 \
    && apt-get install -y python3-pip

# INSTALL PROJECT-SPECIFIC DEPENDENCIES
COPY . /vente-privee
RUN pip3 install -r vente-privee/requirements.txt && cd vente-privee && pip3 install -e .
RUN pip3 install gunicorn

WORKDIR vente-privee
ENV FLASK_APP vente_privee/app.py

# RUN APPLICATION
CMD gunicorn -b :5003 --access-logfile - --error-logfile - vente_privee.app:app

