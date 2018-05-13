import json
import app_config
import logging
import logger


logger.init_logger()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def load_coordinates(*args):
    try:
        json_path = app_config.COORDINATES_FILE_PATH
        json_data = json.load(open(json_path))
        LOGGER.info(f'Loaded coordinates data from file: {json_data}')

        return json_data['coordinates']

    except (Exception) as arg:
        LOGGER.info(f'An error was fetched:\n{arg}')
        raise arg


if __name__ == '__main__':
    coordinates = load_coordinates()
    for pair in coordinates:
        # print(pair)
        print(f'Latitude {pair["lat"]} | Longitude: {pair["lon"]}')