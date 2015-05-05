#!/usr/bin/env bash

# Start initial services at boot
# NOTE: the start order is significant
SERVICES="
	registry
	#auth
	#fleet-ui	
	#mongo
	#oauth
	#redis
	"
for svs in $SERVICES ; do
	unit=/var/lib/apps/$svs/units/$svs.service
	if [ -f $unit ]; then
		if [ ! $(fleetctl list-units | grep $unit grep $unit > /dev/null 2>&1) ]; then
			echo fleetctl destroy $unit
			fleetctl destroy $unit > /dev/null 2>&1
		fi
		echo fleetctl start $unit
		fleetctl start $unit
	fi
done
