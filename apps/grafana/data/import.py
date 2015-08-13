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

# Data source
DATA_SOURCE='google'
DATA_SOURCE_URL = 'http://www.google.com/finance/historical?output=csv&q='

# InfluxDB connections settings
HOST = '172.17.8.101'
PORT = '8086'
DB = 'sp500'
DB_USER = 'root'
DB_PASS = 'root@work'
ENDPOINT = 'write'
PRECISION='s'
DB_URL = "http://%s:%s/%s?db=%s&precision=%s" \
    % (HOST, PORT, ENDPOINT, DB, PRECISION)


def main(args):
    if args['<symbol>']:
        stock = args['<symbol>']
        try:
            data = get_data(stock)
            for line in data.splitlines():
                if line[0].isdigit():
                    add_datapoint(stock, line.rstrip())
        except ValueError,e:
            print(e)
            print(__doc__)
            sys.exit(1)

def get_data(symbol):
    r = requests.get(DATA_SOURCE_URL+symbol)
    if r.status_code != 200:
        #print r.text
        raise ValueError("Error: Symbol Not Found")
    else:
        return r.text
                    
def add_datapoint(measurement, data):
    post_data = marshall_datapoint(measurement, data)
    #print post_data
    r = requests.post(DB_URL, auth=(DB_USER, DB_PASS), data=post_data)
    if r.status_code != 204:
        print r.status_code, r.text
    else:
        print "Datapoint added: ", post_data

def marshall_datapoint(measurement, data):
    v_date, v_open, v_high, v_low, v_close, v_volume = data.split(',')
    v_time = time.mktime(datetime.datetime.strptime(v_date, "%d-%b-%y").timetuple())
    v_time = int(v_time)
    tags = "source=%s" % DATA_SOURCE
    fields = "open=%s,high=%s,low=%s,close=%s,volume=%s" \
        % (v_open, v_high, v_low, v_close, v_volume)
    return "%s,%s %s %s" % (measurement, tags, fields, v_time)

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)

    # To manually submit data points which are not yet written, call commit:
    #MySeriesHelper.commit()
