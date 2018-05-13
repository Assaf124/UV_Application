import os


OPENUV_TOKEN = '92096e5152c61f0d3f5c64a3e89fa55e'
NOAA_TOKEN = 'IErLDmdrwFDWwXGWagebjjYVlOSsvmqV'
GOOGLE_API_KEY = 'AIzaSyDRZy0h1Tl5Q1CCctsjysXDt7itqS9-UJQ'
APPLICATION_MAIN_PATH = r'C:\myDirectory\uvApplication'
COORDINATES_DIR_NAME = 'Coordinates'
COORDINATES_FILE_NAME = 'coordinates.json'
COORDINATES_FILE_PATH = os.path.join(APPLICATION_MAIN_PATH, COORDINATES_DIR_NAME, COORDINATES_FILE_NAME)
CSV_DIR_NAME = 'xls_files'
CSV_FILE_NAME = 'uv_risks.csv'
LOGS_DIR_NAME = 'Logging'
LOG_FILE_NAME = 'program.log'
LOG_FILE_PATH = os.path.join(APPLICATION_MAIN_PATH, LOGS_DIR_NAME, LOG_FILE_NAME)
LOG_FILE_MODE = 'w'  # a = append , w = overwrite


if not os.path.exists(APPLICATION_MAIN_PATH):
    os.makedirs(APPLICATION_MAIN_PATH)

csv_files_dir = os.path.join(APPLICATION_MAIN_PATH, CSV_DIR_NAME)
if not os.path.exists(csv_files_dir):
    os.makedirs(csv_files_dir)

log_files_dir = os.path.join(APPLICATION_MAIN_PATH, LOGS_DIR_NAME)
if not os.path.exists(log_files_dir):
    os.makedirs(log_files_dir)
    os.mknod(LOG_FILE_PATH)

coordinates_file_dir = os.path.join(APPLICATION_MAIN_PATH, COORDINATES_DIR_NAME)
if not os.path.exists(coordinates_file_dir):
    os.makedirs(coordinates_file_dir)
    os.mknod(COORDINATES_FILE_PATH)