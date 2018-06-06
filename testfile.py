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


def load_coordinates_new(*args):

    json_path = app_config.ALT_COORDINATES_FILE_PATH
    json_data = json.load(open(json_path))
    # LOGGER.info(f'Loaded coordinates data from file: {json_data}')

    return json_data['coordinates']


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
    # LAT = 1.3521
    # LNG = 103.8198

    # location = 'uk/london'
    # method = 'GET'
    # url = f'https://www.timeanddate.com/sun/{location}'
    # dict_headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #                 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    #
    #
    # http = urllib3.PoolManager()
    # http_request = http.request(method, url, headers=dict_headers)
    # LOGGER.info(f'Sent http request: {method}  {url}, {dict_headers}')
    #
    # # encoded_body = 'grant_type=client_credentials'
    # # http_request = http.request(method, url, headers=dict_headers, body=encoded_body)
    #
    # reply = http_request.data.decode('utf-8')


    APP_ACCESS_KEY = 'FGc5t40NnH'

    url = f'https://api.xmltime.com/astronomy?accesskey={APP_ACCESS_KEY}&expires=2018-06-04T14%3A08%3A49%2B00%3A00' \
          f'&signature=6%2FIh4VRdLFDEVfibWYaCF3roya8%3D&version=2&object=sun&placeid=uk%2Flondon' \
          f'&startdt=2018-06-04&types=current'

    APP_ID = 'a3562ce1'
    APP_KEY = '3c9735afcc225ebc3e503c83c06f98be'

    API_KEY = app_config.SOLCAST_API_KEY
    url = f'https://api.solcast.com.au/radiation/forecasts?latitude={LAT}&longitude={LNG}&api_key={API_KEY}&format=json'


    # url = f'http://api.weatherunlocked.com/api/trigger/{LAT},{LNG}/current humidity gt 16 includecurrent?' \
    #       f'app_id={APP_ID}&app_key={APP_KEY}'

    # url = f'http://api.weatherunlocked.com/api/trigger/{LAT},{LNG}/current utctime?' \
    #       f'app_id={APP_ID}&app_key={APP_KEY}'

    # url = f'http://api.weatherunlocked.com/api/trigger/{LAT},{LNG}/current cloud gt 0 includecurrent?' \
    #       f'app_id={APP_ID}&app_key={APP_KEY}'


    # method = 'GET'
    #
    # http = urllib3.PoolManager()
    # http_request = http.request(method, url)
    #
    # # reply = http_request.data.decode('utf-8')
    # reply = json.loads(http_request.data.decode('utf-8'))
    # print(reply['forecasts'])
    # print(reply['forecasts'][0]['period_end'])
    # print(reply['forecasts'][0]['cloud_opacity'])
    # print(reply['forecasts'][0]['dni'])
    # print(reply['forecasts'][0]['dhi'])

    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S')
    print(timestamp)
