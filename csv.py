import os
import logging
import logger


logger.init_logger()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def create_csv_file(csv_file_dir, csv_file_name, *args):

    LOGGER.info(f'create_csv_file function was called with parameters: {csv_file_dir}, {csv_file_name}')
    if not os.path.exists(csv_file_dir):
        os.makedirs(csv_file_dir)

    file_name = csv_file_name
    path = os.path.join(csv_file_dir, file_name)
    file = open(path, "w")
    file.write('Local Time, City, Latitude, Longitude, st1, st2, st3, st4, st5, st6, Cloud Coverage (%), '
               'Solar (Wh/m^2), Sun Angle\n')
    file.close()
    LOGGER.info('csv file was created successfully')

    return


def add_entry_to_csv_file(csv_file_dir, file_name, current_local_time, LAT, LNG, uv_risk1, uv_risk2, uv_risk3,
                          uv_risk4, uv_risk5, uv_risk6, cloud_coverage, solar, angle, *args):

    LOGGER.info(f'add_entry function was called with parameters: {csv_file_dir}, {file_name}')
    path = os.path.join(csv_file_dir, file_name)
    file = open(path, "a")
    # file.write('Time, Latitude, Longitude, st2, st3, st4, Clouds Coverage\n')
    file.write('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(current_local_time, 'City', LAT, LNG, uv_risk1,
                                                                 uv_risk2, uv_risk3, uv_risk4, uv_risk5,
                                                                 uv_risk6, cloud_coverage, solar, angle))
    file.close()
    LOGGER.info('Add entry to csv file')

    return