import subprocess
import json
import re


# This scripts retrieves the current installed version of list of applications + its last update date


json_path = r'C:\myDirectory\uvApplication\UV_Application\General_Info\applications_info.json'
json_data = json.load(open(json_path))
info_list = json_data['applications_info']

'''
application_info = {'Whatsapp': 'https://play.google.com/store/apps/details?id=com.whatsapp',
                    'Viber':    'https://play.google.com/store/apps/details?id=com.viber.voip',
                    'Telegram': 'https://play.google.com/store/apps/details?id=org.telegram.messenger',
                    'Skype':    'https://play.google.com/store/apps/details?id=com.skype.raider',
                    'Tango':    'https://play.google.com/store/apps/details?id=com.sgiggle.production',
                    'Zalo':     'https://play.google.com/store/apps/details?id=com.zing.zalo',
                    'Facebook': 'https://play.google.com/store/apps/details?id=com.facebook.katana',
                    'Facebook msn': 'https://play.google.com/store/apps/details?id=com.facebook.orca'}

for app_name, app_url in application_info.items():

    url = app_url
    method = 'GET'

    http = urllib3.PoolManager()
    http_request = http.request(method, url)

    reply = http_request.data.decode('utf-8')

    reply_split_1 = reply.split('<span class="htlgb"><div><span class="htlgb">')
    reply_split_2 = reply_split_1[1].split('</span>')
    last_updated = reply_split_2[0]

    print(f'{app_name}:  {last_updated}')
    '''

command = 'adb shell dumpsys package'
paceage = 'com.whatsapp'
execute = f'{command} {paceage}'

output = subprocess.check_output(execute, shell=True)
output_str = str(output)

re_compiled = re.compile('versionName=(\d*[.]\d*[.]\d*)')
version = re_compiled.search(output_str).groups(0)
print(f'Installed version:  {version[0]}')

re_compiled = re.compile('lastUpdateTime=(\d*[-]\d*[-]\d*)')
update_time = re_compiled.search(output_str).groups(0)
print(f'Last updated:  {update_time[0]}')