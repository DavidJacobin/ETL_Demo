import os
import sys
import petl
import pymssql
import configparser
import requests
import datetime
import json
import decimal

# get data from config file

config = configparser.ConfigParser()
try:
    config.read('ETLDemo.ini')
except Exception as e:
    print('could not read ETLDemo.ini' + str(e))
    sys.exit()

# reading settings from config file
start_date = config['CONFIG']['start_date']
url = config['CONFIG']['url']
server = config['CONFIG']['server']
database = config['CONFIG']['database']

# request data from url
try:
    Response = requests.get(url+start_date)
except Exception as e:
    print('could not read request')
    sys.exit()

#print(Response.text)

# lists for data storage

Dates = []
Rates = []

# response in to json
if Response.status_code == 200:
    Raw_info = json.loads(Response.text)

    for row in Raw_info['observations']:
        Dates.append(datetime.datetime.strptime(row['d'], '%Y-%m-%d'))
        Rates.append(decimal.Decimal(row['FXUSDCAD']['v']))

    # creating petl table
    exchange_Rates = petl.fromcolumns([Dates, Rates], header=['date', 'rate'])

print(exchange_Rates)