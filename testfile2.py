import urllib3
import subprocess
import json
import re


# This scripts retrieves the current installed version of list of applications + its last update date


def check_app_last_update(app_url, *args):

    url = app_url
    method = 'GET'

    http = urllib3.PoolManager()
    http_request = http.request(method, url)

    reply = http_request.data.decode('utf-8')

    reply_split_1 = reply.split('<span class="htlgb"><div><span class="htlgb">')
    reply_split_2 = reply_split_1[1].split('</span>')
    last_updated = reply_split_2[0]
    # print(f'{app_name}:  {last_updated}')

    return last_updated


# ******   program starts here   ******


json_path = r'C:\myDirectory\uvApplication\UV_Application\General_Info\applications_info.json'
json_data = json.load(open(json_path))
app_list = json_data['applications_info']

for app in app_list:
    app_name = app["application_name"]
    package = app["google_play_id"]
    google_play_link = app["google_play_link"]

    # print(f'{app_name}\n{package}\n{google_play_link}\n\n')

    command = 'adb shell dumpsys package'
    execute = f'{command} {package}'

    output = subprocess.check_output(execute, shell=True)
    output_str = str(output)

    # retrieve the application installed version
    re_compiled = re.compile('versionName=(\d*[.]\d*[.]\d*)')
    version = re_compiled.search(output_str).groups(0)
    # print(f'Installed version:  {version[0]}')

    # retrieve the application last update date
    re_compiled = re.compile('lastUpdateTime=(\d*[-]\d*[-]\d*)')
    update_time = re_compiled.search(output_str).groups(0)
    # print(f'Last updated:  {update_time[0]}')

    # retrieve the application latest market update
    app_market_version = check_app_last_update(google_play_link)

    print(f'Application:\t\t\t{app_name}\nInstalled version:\t\t{version[0]}\nWas last updated in:\t{update_time[0]}\nMarket last update:\t\t{app_market_version}')