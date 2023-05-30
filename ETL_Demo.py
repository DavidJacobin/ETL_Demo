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

print(Response.text)
