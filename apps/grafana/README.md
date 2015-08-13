# Stock Market Dashboard Example 

## Start Apps Server

```
fleetctl start units/*.service
```

## Import Stock Historical Data

```
$ data/import.py aapl
$ data/import.py ibm
$ data/import.py goog
```

## Setup Stock Market Dashboard 

```
Go to http://172.17.8.101:3000

login as admin/admin

import etc/dashboards/SP500.json into grafana dashboards

```