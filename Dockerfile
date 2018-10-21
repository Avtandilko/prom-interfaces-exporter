FROM python:3.6.4-alpine

ENV APP_FILE app/prom-interfaces-exporter.py
VOLUME /sys/class/net/:/host/sys/class/net/:ro

RUN mkdir /app
COPY src/prom-interfaces-exporter.py /app/

EXPOSE 9425
ENTRYPOINT ["sh", "-c", "python /app/prom-interfaces-exporter.py"]
