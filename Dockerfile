FROM python:3.6.4-alpine

ENV APP_FILE /prom-interfaces-exporter/prom-interfaces-exporter.py

RUN mkdir /prom-interfaces-exporter
COPY prom-interfaces-exporter.py /prom-interfaces-exporter/
EXPOSE 9425
ENTRYPOINT ["sh", "-c", "python /prom-interfaces-exporter/prom-interfaces-exporter.py"]
