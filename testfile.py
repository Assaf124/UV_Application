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
    LAT = 46.4825
    LNG = 30.7233

    # New York
    # LAT = 40.7128
    # LNG = -74.0061

    # Singapore
    # LAT = 1.3521
    # LNG = 103.8198

    # location = 'uk/london'
    # method = 'GET'
    # url = f'https://www.timeanddate.com/sun/{location}'
    #
    # http = urllib3.PoolManager()
    # http_request = http.request(method, url)
    #
    # reply = http_request.data.decode('utf-8')
    #
    # 'Sun Altitude: </span><span id=sunalt>50.8°</span></p>'
    #
    # reply_split_1 = reply.split('<span id=sunalt>')
    # reply_split_2 = reply_split_1[1].split('</span></p><p>')
    # print(f'Sun altitude: {reply_split_2[0]}')

    coordinates = load_coordinates_new()

    for item in coordinates:
        LAT = item["lat"]
        LNG = item["lon"]
        COUNTRY = item["Main Place"]
        CITY = item["Place"]
        print(LAT, LNG, COUNTRY, CITY)