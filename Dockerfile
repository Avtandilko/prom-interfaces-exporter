FROM python:3.6.4-alpine
RUN mkdir /prom-interface-exporter
COPY prom-interface-exporter.py /prom-interface-exporter/
ENTRYPOINT ["sh", "-c", "python /prom-interface-exporter/prom-interface-exporter.py"]
