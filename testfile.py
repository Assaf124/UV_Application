import app_config
import logging
import logger
import urllib3
import json
import datetime
import data
import csv
import parse_coordinates
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


if __name__ == '__main__':
    # Herzeliya
    LAT = 32.15922
    LNG = 34.80715

    # New York
    # LAT = 40.7128
    # LNG = -74.0061

    # Singapore
    # LAT = 1.3521
    # LNG = 103.8198

    latitude = LAT
    longitude = LNG

    # reply = get_noaa_data()
    # print(reply)

    # day_of_year = time.localtime().tm_yday
    # print(day_of_year)

    # RAD = math.pi/180
    # EARTH_TILT = 23.43691
    #
    # print(LAT)
    #
    # for day_of_year in range(1,366):
    #     LAMBDA = EARTH_TILT * RAD * math.sin(RAD*(360/365.2425)*(284 + day_of_year))
    #     NOON_ANGLE = 90 - LAT + math.degrees(LAMBDA)
    #     print(day_of_year, math.degrees(LAMBDA), NOON_ANGLE)



    # coords = {'longitude': LNG, 'latitude': LAT}
    #
    # sun = Sun()
    # LOCAL_TIME_OFFSET = 3
    # # Sunrise time UTC (decimal, 24 hour format)
    #
    # sunrise_hour = math.floor(sun.get_sunrise_time(coords)['decimal'] + LOCAL_TIME_OFFSET)
    # sunrise_minutes = 60*(sun.get_sunrise_time(coords)['decimal'] + LOCAL_TIME_OFFSET - sunrise_hour)
    # print(f'{sunrise_hour}:{int(sunrise_minutes)}')
    #
    # # Sunset time UTC (decimal, 24 hour format)
    # sunset_hour = math.floor(sun.get_sunset_time(coords)['decimal'] + LOCAL_TIME_OFFSET)
    # sunset_minutes = 60*(sun.get_sunset_time(coords)['decimal'] + LOCAL_TIME_OFFSET - sunset_hour)
    # print(f'{sunset_hour}:{int(sunset_minutes)}')
    #
    # daylength = sun.get_sunset_time(coords)['decimal'] - sun.get_sunrise_time(coords)['decimal']
    # print(daylength)






    # sun = Sun()
    # LOCAL_TIME_OFFSET = 3
    # # Sunrise time UTC (decimal, 24 hour format)
    #
    # sunrise_hour = math.floor(sun.get_sunrise_time(LAT, LNG)['decimal'] + LOCAL_TIME_OFFSET)
    # sunrise_minutes = 60*(sun.get_sunrise_time(LAT, LNG)['decimal'] + LOCAL_TIME_OFFSET - sunrise_hour)
    # print(f'{sunrise_hour}:{int(sunrise_minutes)}')
    #
    # # Sunset time UTC (decimal, 24 hour format)
    # sunset_hour = math.floor(sun.get_sunset_time(LAT, LNG)['decimal'] + LOCAL_TIME_OFFSET)
    # sunset_minutes = 60*(sun.get_sunset_time(LAT, LNG)['decimal'] + LOCAL_TIME_OFFSET - sunset_hour)
    # print(f'{sunset_hour}:{int(sunset_minutes)}')
    #
    # daylength = sun.get_sunset_time(LAT, LNG)['decimal'] - sun.get_sunrise_time(LAT, LNG)['decimal']
    # print(daylength)
    #
    #
    #
    # print(datetime.datetime.utcnow())
    #
    # data.get_local_time(LAT, LNG)        #   dstOffset and rawOffset are given in seconds

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1526310489.7946904)))

