import os
import logging
import logger


# logger.init_logger()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def create_csv_file(csv_file_dir, csv_file_name, *args):

    LOGGER.info(f'create_csv_file function was called with parameters: {csv_file_dir}, {csv_file_name}')

    if not os.path.exists(csv_file_dir):
        os.makedirs(csv_file_dir)

    file_name = csv_file_name
    path = os.path.join(csv_file_dir, file_name)
    file = open(path, "w")
    file.write('Local Time, Location, Latitude, Longitude, st1, st2, st3, st4, st5, st6, Ozone (Dobson), '
               'Cloud Coverage (%), DNI, DHI, GHI, Sun Altitude (Degree)\n')
    file.close()
    LOGGER.info('csv file was created successfully')

    return


def add_entry_to_csv_file(csv_file_dir, file_name, current_local_time, location, LAT, LNG, uv_risk1, uv_risk2, uv_risk3,
                          uv_risk4, uv_risk5, uv_risk6, ozone, cloud_coverage, dni, dhi, ghi, altitude, *args):

    LOGGER.info(f'add_entry function was called with parameters: {csv_file_dir}, {file_name}')
    path = os.path.join(csv_file_dir, file_name)
    file = open(path, "a")

    file.write(f'{current_local_time}, {location}, {LAT}, {LNG}, {uv_risk1}, {uv_risk2}, {uv_risk3}, {uv_risk4}, '
               f'{uv_risk5}, {uv_risk6}, {ozone}, {cloud_coverage}, {dni}, {dhi}, {ghi}, {altitude}\n')

    file.close()
    LOGGER.info('Added entry to csv file')

    return