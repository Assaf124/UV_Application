import os
import logging
import logger


# logger.init_logger()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def create_csv_file(csv_file_dir, csv_file_name, *args):
    """
    This function creates a csv file according to the arguments passes to it.
    See below description.

    Args:
        csv_file_dir:   String. Defines the csv file directory path
        csv_file_name:  String. Defines the csv file name
    """    
    
    LOGGER.info(f'create_csv_file function was called with parameters: {csv_file_dir}, {csv_file_name}')

    if not os.path.exists(csv_file_dir):
        os.makedirs(csv_file_dir)

    file_name = csv_file_name
    path = os.path.join(csv_file_dir, file_name)
    file = open(path, "w")
    file.write('Local Time, Location, Latitude, Longitude, S.T1, S.T2, S.T3, S.T4, S.T5, S.T6, UV Index, '
               'Ozone (Dobson), Cloud Coverage (%), Precipitation (%), DNI (W/m^2), DHI (W/m^2), GHI (W/m^2), '
               'Sun Altitude (Degree)\n')
    file.close()
    LOGGER.info('csv file was created successfully')

    return


def add_entry_to_csv_file(csv_file_dir, file_name, current_local_time, location, LAT, LNG, uv_risk1, uv_risk2, uv_risk3,
                          uv_risk4, uv_risk5, uv_risk6, uv_index, ozone, cloud_coverage, precipitation, dni, dhi, ghi,
                          altitude, *args):
    """
    This function add entries to the program .csv file according to the arguments passes to it.
    See below description.

    Args:
        csv_file_dir:       String. Defines the csv file directory path
        file_name:          String.
        current_local_time: String.
        location:           String.
        LAT:                Integer. the latitude of the given location
        LNG:                Integer. the longitude of the given location
        uv_risk1-6:         Integer. The safe exposure time for different skin types (1 to 6)
        uv_index:           Integer. UV index -> https://en.wikipedia.org/wiki/Ultraviolet_index
        ozone:              Integer.
        cloud_coverage:     Integer.
        precipitation:      Integer.
        dni:                Integer. Direct Normal Irradiance
        dhi:                Integer. Diffuse Horizontal Irradiance
        ghi:                Integer. Global Horizontal Irradiance
        altitude:           Integer. Sun altitude angle (in the sky)
    """
    
    LOGGER.info(f'add_entry function was called with parameters: {csv_file_dir}, {file_name}')
    path = os.path.join(csv_file_dir, file_name)
    file = open(path, "a")

    file.write(f'{current_local_time}, {location}, {LAT}, {LNG}, {uv_risk1}, {uv_risk2}, {uv_risk3}, {uv_risk4}, '
               f'{uv_risk5}, {uv_risk6}, {uv_index}, {ozone}, {cloud_coverage}, {precipitation}, {dni}, {dhi}, {ghi}, '
               f'{altitude}\n')

    file.close()
    LOGGER.info('Added entry to csv file')

    return
