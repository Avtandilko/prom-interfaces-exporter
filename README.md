# Prometheus interfaces exporter

|             | status |
|-------------|------------|
| **master** | [![Build Status](https://travis-ci.org/Avtandilko/prom-interfaces-exporter.svg?branch=master)](https://travis-ci.org/Avtandilko/prom-interfaces-exporter) |

## Docker build
```
git clone https://github.com/Avtandilko/prom-interfaces-exporter.git
docker build -t avtandilko/prom-interfaces-exporter prom-interfaces-exporter
docker push avtandilko/prom-interfaces-exporter
```
## Docker usage
```
docker run -d -p 9425:9425 -v /sys:/host/sys:ro --name prom-interfaces-exporter avtandilko/prom-interfaces-exporter
```
