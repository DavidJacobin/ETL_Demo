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