import app_config
import logging
import logger
import datetime
import data
import csv
import json_parser


# Initializing the logger
logger.init_logger()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
LOGGER.info('************      Program Started      ************\n')


# Setting the xls file and directory
CSV_FILE_DIR = app_config.csv_files_dir
CSV_FILE_NAME = app_config.CSV_FILE_NAME
csv.create_csv_file(CSV_FILE_DIR, CSV_FILE_NAME)


# Main program starts here


# loading Latitude and Longitude coordinates
coordinates = json_parser.load_coordinates()

for pair in coordinates:
    LAT = pair["lat"]
    LNG = pair["lon"]

    current_local_time, local_time_unix_format, time_offset = data.get_local_time(LAT, LNG)

    location = data.get_location(LAT)

    uv_risk = data.get_uv_risk(LAT, LNG, 'x-access-token')
    LOGGER.info(f'Received uv risk values: {uv_risk}')

    access_token = data.get_token_for_clouds_coverage()
    LOGGER.info(f'Received access token for cloud coverage: {access_token}')

    cloud_coverage, solar = data.get_cloud_coverage(LAT, LNG, access_token)
    LOGGER.info(f'Received cloud coverage value: {cloud_coverage}')
    LOGGER.info(f'Received Solar amount value: {solar}')

    sun_angle = data.calculate_sun_angle(LAT, LNG, local_time_unix_format, time_offset)

    csv.add_entry_to_csv_file(CSV_FILE_DIR, CSV_FILE_NAME, current_local_time, location,
                              LAT, LNG, uv_risk[0], uv_risk[1], uv_risk[2],
                              uv_risk[3], uv_risk[4], uv_risk[5],cloud_coverage, solar, sun_angle)

    # print(current_local_time, uv_risk, cloud_coverage, solar, sun_angle)
