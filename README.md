# prom-interface-exporter

## Docker build
git clone https://github.com/Avtandilko/prom-interface-exporter.git
docker build -t avtandilko/prom-interface-exporter prom-interface-exporter
docker push avtandilko/prom-interface-exporter

## Docker usage
docker run -d -p 9425:9425 -v /sys:/host/sys:ro --name prom-interface-exporter avtandilko/prom-interface-exporter

