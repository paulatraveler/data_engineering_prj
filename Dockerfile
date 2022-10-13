FROM rocker/r-base:latest

MAINTAINER Paula Kmicinska <p.kmicinska@gmail.com>


# INSTALL PYTHON
RUN apt-get update \
    && apt-get install -y python3.6 \
    && apt-get install -y python3-pip

# INSTALL PROJECT-SPECIFIC DEPENDENCIES
COPY . /data_engineering_prj
RUN pip3 install -r data_engineering_prj/requirements.txt && cd data_engineering_prj && pip3 install -e .
RUN pip3 install gunicorn

WORKDIR data_engineering_prj
ENV FLASK_APP data_engineering_prj/app.py

# RUN APPLICATION
CMD gunicorn -b :5003 --access-logfile - --error-logfile - data_engineering_prj.app:app

