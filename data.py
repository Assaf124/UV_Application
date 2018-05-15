import app_config
import urllib3
import json
import time
import datetime
import logging
import logger
import math
import json_parser


# logger.init_logger()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def get_location(latitude, *args):
    location_dict = json_parser.load_locations()

    for key, value in location_dict.items():
        if value == latitude:
            return key

    return None


def get_uv_risk(latitude, longitude, header_name, *args):

    method = 'GET'
    token_value = app_config.OPENUV_TOKEN
    url = 'http://api.openuv.io/api/v1/uv?lat={}&lng={}'.format(latitude, longitude)
    dict_headers = {header_name: token_value}

    try:
        http = urllib3.PoolManager()

        http_request = http.request(method, url, headers=dict_headers)
        LOGGER.info(f'Sent http request: {method}  {url}, {dict_headers}')

        reply = json.loads(http_request.data.decode('utf-8'))
        LOGGER.info(f'Got reply: {reply}')

        uv_dict = reply['result']['safe_exposure_time']
        uv_list = list(uv_dict.values())
        LOGGER.info(f'Returning uv values: {uv_list}')

        return uv_list

    except Exception as arg:
        LOGGER.error(f'An error was fetched:\n{arg}')
        raise arg


def get_token_for_clouds_coverage(*args):

    method = 'POST'
    url = 'https://api.awhere.com/oauth/token'
    dict_headers = {'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'Basic QWowMnFJZTFVSWdxbWJ4Y2NzY1QyeGFTZU9Xa3QybHI6bWt5RG42dnIxRHhZR0RtNQ=='}
    encoded_body = 'grant_type=client_credentials'

    try:
        http = urllib3.PoolManager()

        http_request = http.request(method, url, headers=dict_headers, body=encoded_body)
        LOGGER.info('Sent http request for token: {}  {}, {} {}'.format(method, url, dict_headers, encoded_body))

        reply = json.loads(http_request.data.decode('utf-8'))
        LOGGER.info('Received access token: {}'.format(reply['access_token']))

        return reply['access_token']

    except (Exception) as arg:
        LOGGER.error(f'An error was fetched:\n{arg}')
        raise arg


def get_cloud_coverage(latitude, longitude, token, *args):

    return 54.3, 732    #   remove this
    today = time.strftime("%Y-%m-%d", time.gmtime())
    method = 'GET'
    url = 'https://api.awhere.com/v2/weather/locations/{},{}/forecasts/{}'.format(latitude, longitude, today)
    dict_headers = {'Authorization': 'Bearer {}'.format(token)}

    try:
        http = urllib3.PoolManager()

        http_request = http.request(method, url, headers=dict_headers)
        LOGGER.info('Sent http request: {}  {}, {}'.format(method, url, dict_headers))

        reply = json.loads(http_request.data.decode('utf-8'))
        LOGGER.info(f'Received forecast reply: {reply}')

        forecast_list = reply['forecast']
        index = parse_list(forecast_list)

        LOGGER.info('Returning cloud coverage value {}'.format(forecast_list[index]['sky']['cloudCover']))
        # print(f"{forecast_list[index]['solar']['amount']}")
        return forecast_list[index]['sky']['cloudCover'], forecast_list[index]['solar']['amount']

    except (Exception) as arg:
        LOGGER.error(f'An error was fetched:\n{arg}')
        raise arg


def parse_list(forecast_list, *args):

    for index, item in enumerate(forecast_list):
        start_datetime_string = item.get('startTime')
        start_time_value = start_datetime_string.split('T')
        hour_value = start_time_value[1].split(':')

        if int(hour_value[0]) == int(datetime.datetime.now().hour):
            return index-1


def get_local_time(latitude, longitude, *args):

    unix_time = time.time()
    LOGGER.info(f'Fetched Unix Epoch Time: {unix_time}')

    api_key = app_config.GOOGLE_API_KEY
    method = 'GET'
    url = f'https://maps.googleapis.com/maps/api/timezone/json?location={latitude},{longitude}&timestamp={unix_time}&' \
          f'key={api_key}'

    try:
        http = urllib3.PoolManager()

        http_request = http.request(method, url)
        LOGGER.info(f'Sent http request: {method} , {url}')

        local_time = json.loads(http_request.data.decode('utf-8'))
        LOGGER.info(f'Received google time reply: {local_time}')

        total_time_offset = local_time['dstOffset'] + local_time['rawOffset']
        actual_local_time = unix_time + total_time_offset

        local_time_human_format = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(actual_local_time))

        return local_time_human_format

    except (Exception) as arg:
        LOGGER.error(f'An error was fetched:\n{arg}')
        raise arg


def calculate_sun_max_angle(latitude):

    RAD = math.pi/180
    EARTH_TILT = 23.43691

    day_of_year = time.localtime().tm_yday

    DELTA = EARTH_TILT * RAD * math.sin(RAD * (360 / 365.2425) * (284 + day_of_year))
    NOON_ANGLE = 90 - latitude + math.degrees(DELTA)

    return NOON_ANGLE


if __name__ == '__main__':

    # Herzeliya
    LAT = 32.15922
    LNG = 34.80715

    # New York
    LAT = 40.7128
    LNG = -74.0061

    # Singapore
    LAT = 1.3521
    LNG = 103.8198

    # Sydney
    LAT = -33.8688
    LNG = 151.2093

    # Lisbon
    LAT = 38.7223
    LNG = -9.1993

    # Beijing
    LAT = 39.9042
    LNG = 116.4074
