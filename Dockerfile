FROM python:3.8
WORKDIR /root
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE fresh_code.settings
COPY . /root
RUN apt-get -y update
RUN apt-get install -y vim
RUN pip install -r /root/requirements.txt