#!/usr/bin/bash
source /var/lib/apps/influxdb/dbpass
docker exec -ti influxdb.service /opt/influxdb/influx -password $INFLUXDB_ADMIN_PWD -username $INFLUXDB_ADMIN_USER $@