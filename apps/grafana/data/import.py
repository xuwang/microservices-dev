#!/usr/bin/env python
"""
Usage:
  import.py <symbol>
  
Options:
  --help        Show this page
  
Arguments:
  <symbol>      A stock symbol name, eg. AAPL, IBM, etc.

"""

import sys
import time
import datetime
from docopt import docopt
import requests
from requests.auth import HTTPBasicAuth
from contextlib import closing

# Data source
DATA_SOURCE='google'
DATA_SOURCE_URL = 'http://www.google.com/finance/historical?output=csv&q='

# InfluxDB connections settings
HOST = '172.17.8.101'
PORT = '8086'
DB = 'sp500'
DB_USER = 'admin'
DB_PASS = 'admin'
DB_WRITE = 'write'
DB_QUERY = 'query'
PRECISION='s'
DB_WRITE_URL = "http://%s:%s/%s?db=%s&precision=%s" % (HOST, PORT, DB_WRITE, DB, PRECISION)
DB_QUERY_URL = "http://%s:%s/%s?db=%s&precision=%s" % (HOST, PORT, DB_QUERY, DB, PRECISION)


def main(args):
    if args['<symbol>']:
        stock = args['<symbol>']
        try:
            with closing(requests.get(DATA_SOURCE_URL+stock, stream=True)) as r:
                if r.status_code != 200:
                    #print r.text
                    raise ValueError("Error: Symbol Not Found")
                else:
                    for line in r.iter_lines():
                        if line[0].isdigit():
                            datapoint = marshall_datapoint(stock, line.rstrip())              
                            add_datapoint(datapoint)
        except ValueError,e:
            print(e)
            print(__doc__)
            sys.exit(1)

def get_datapoint(measurement, t):
    query = "select * from %s where time=%ss" % (measurement, t)
    params = {"q":query}
    r = requests.get(DB_QUERY_URL, auth=(DB_USER, DB_PASS), params=params)
    if r.status_code != 200:
        raise ValueError("Error: %s %s" % r.status_code, r.text)
    else:
        return r.text
                    
def add_datapoint(data):
    dp = get_datapoint(data["measurement"], data["time"])
    # insert the datapoint iff it's not in the db
    if "time" in dp:
        print "Datapoint exist: ", dp
    else:
        post_data ="%s,%s %s %s" \
            % (data["measurement"], data["tags"], data["fields"], data["time"])
        #print post_data
        r = requests.post(DB_WRITE_URL, auth=(DB_USER, DB_PASS), data=post_data)
        if r.status_code != 204:
            print r.status_code, r.text
        else:
            print "Datapoint added: ", post_data

def marshall_datapoint(measurement, data):
    v_date, v_open, v_high, v_low, v_close, v_volume = data.split(',')
    v_time = time.mktime(datetime.datetime.strptime(v_date + " 17:00:00", "%d-%b-%y %H:%M:%S").timetuple())
    v_time = int(v_time)
    tags = "source=%s" % DATA_SOURCE
    fields = "open=%s,high=%s,low=%s,close=%s,volume=%s" % (v_open, v_high, v_low, v_close, v_volume)
    return {"measurement":measurement, "tags":tags, "fields":fields, "time":v_time}

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)

    # To manually submit data points which are not yet written, call commit:
    #MySeriesHelper.commit()
