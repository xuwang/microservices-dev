#!/usr/bin/env bash

# Start initial services at boot
# NOTE: the start order is significant
SERVICES="
	registry
	redis
	mongo
	"
for svs in $SERVICES ; do
	unit=/var/lib/apps/$svs/units/$svs.service
	if [ -f $unit ]; then
		echo fleetctl start $unit
		fleetctl start $unit
	fi
done
