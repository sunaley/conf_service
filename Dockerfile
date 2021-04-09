FROM python:3.9-slim

COPY . /opt/conf_service

RUN pip install -r /opt/conf_service/requirements.txt

WORKDIR /opt/conf_service

ENTRYPOINT [ "/opt/conf_service/entrypoint.sh" ]