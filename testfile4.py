import time
import sched
import datetime
import os


scheduler = sched.scheduler(time.time, time.sleep)


def run_my_code():
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d__UTC%H-%M-%S')
    print(f'{timestamp}:  Run the code...')
    os.system('python uv_vs_clouds.py')
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d__UTC%H-%M-%S')
    print(f'{timestamp}:  code execution ended...')


def my_scheduler():
    scheduler.enter(0, 1, run_my_code, ())
    scheduler.run()
    time.sleep(3540)


for i in range(4):
    my_scheduler()