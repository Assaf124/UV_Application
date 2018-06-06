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


# Setting the csv file and directory
timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d__UTC%H-%M-%S')
CSV_FILE_DIR = app_config.csv_files_dir
CSV_FILE_NAME = app_config.CSV_FILE_NAME + '__' + str(timestamp) + '.csv'
csv.create_csv_file(CSV_FILE_DIR, CSV_FILE_NAME)


# Main program starts here


# loading Latitude and Longitude coordinates
coordinates = json_parser.load_coordinates()


for coordinate_item in coordinates:
    LAT = coordinate_item["lat"]
    LNG = coordinate_item["lon"]
    LOGGER.info(f'** New loop cycle started for latitude: {LAT} and longitude: {LNG} **\n')

    location = coordinate_item["Display Place"]
    LOGGER.info(f'Location for given latitude and longitude: {location}')

    current_local_time, local_time_unix_format, time_offset = data.get_local_time(LAT, LNG)

    uv_risk, ozone = data.get_uv_risk(LAT, LNG)
    LOGGER.info(f'Received uv risk values: {uv_risk}')
    LOGGER.info(f'Received Ozone values: {ozone}')

    # access_token = data.get_token_for_clouds_coverage()
    # LOGGER.info(f'Received access token for cloud coverage: {access_token}')

    # cloud_coverage, solar = data.get_cloud_coverage(LAT, LNG, access_token)
    # LOGGER.info(f'Received cloud coverage value: {cloud_coverage}')
    # LOGGER.info(f'Received Solar amount value: {solar}')

    # cloud_coverage = data.get_cloud_coverage_weatherunlocked(LAT, LNG)
    # cloud_coverage = data.get_cloud_coverage_solcast(LAT, LNG)
    # solar = 429

    cloud_coverage, dni, dhi, ghi = data.get_combined_data_solcast(LAT, LNG)

    # sun_angle = data.calculate_sun_angle(LAT, LNG, local_time_unix_format, time_offset)
    sun_altitude = data.get_sun_altitude(coordinate_item["Main Place"], coordinate_item["Place"])

    csv.add_entry_to_csv_file(CSV_FILE_DIR, CSV_FILE_NAME, current_local_time, location, LAT, LNG, uv_risk[0],
                              uv_risk[1], uv_risk[2], uv_risk[3], uv_risk[4], uv_risk[5],ozone, cloud_coverage,
                              dni, dhi, ghi, sun_altitude)


