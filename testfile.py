import app_config
import logging
import logger
import urllib3
import json
import datetime
import data
import csv
import json_parser
import math
import time
from Sun import Sun
import subprocess


logger.init_logger()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def get_noaa_data(*args):

    method = 'GET'
    token_value = app_config.NOAA_TOKEN
    url = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories'
    dict_headers = {'token': token_value}

    try:
        http = urllib3.PoolManager()

        http_request = http.request(method, url, headers=dict_headers)
        LOGGER.info(f'Sent http request: {method}  {url}, {dict_headers}')

        reply = json.loads(http_request.data.decode('utf-8'))
        LOGGER.info(f'Got reply: {reply}')

        return reply

    except Exception as arg:
        LOGGER.error(f'An error was fetched:\n{arg}')
        raise arg


if __name__ == '__main__':
    # Herzeliya
    LAT = 32.15922
    LNG = 34.80715

    # Milan
    LAT = 45.4642
    LNG = 9.1901

    # Odesa
    # LAT = 46.4825
    # LNG = 30.7233

    # New York
    # LAT = 40.7128
    # LNG = -74.0061

    # Singapore
    LAT = 1.3521
    LNG = 103.8198

    # Oslo
    # LAT = 59.9139
    # LNG = 10.7522
    #
    # # Mumbai
    # LAT = 19.0760
    # LNG = 72.8777
    #
    # # Bangkok
    # LAT = 13.7563
    # LNG = 100.5018

    latitude = LAT
    longitude = LNG

    # appid = app_config.OPENWEATHERMAP_KEY
    # method = 'GET'
    # url = f'http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LNG}&appid={appid}'
    #
    # http = urllib3.PoolManager()
    # http_request = http.request(method, url)
    #
    # reply = json.loads(http_request.data.decode('utf-8'))
    # print(reply)


    app_id = app_config.WEATHERUNLOCKED_APP_ID
    app_key = app_config.WEATHERUNLOCKED_APP_KEY

    url = f'http://api.weatherunlocked.com/api/trigger/{latitude},{longitude}/current cloud gt 0 includecurrent?' \
          f'app_id={app_id}&app_key={app_key}'

    method = 'GET'

    http = urllib3.PoolManager()
    http_request = http.request(method, url)
    reply = json.loads(http_request.data.decode('utf-8'))
    print(reply['CurrentWeather'])

