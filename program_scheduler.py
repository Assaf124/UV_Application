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


def my_scheduler(index):
    scheduler.enter(0, 1, run_my_code, ())
    scheduler.run()
    print(f'Finished cycle {index}')
    time.sleep(3540)


def night_sleep(hours):
    for hour in range(hours):
        timestamp1 = datetime.datetime.utcnow().strftime('%Y-%m-%d__UTC%H-%M-%S')
        print(f'took timestamp at:  {timestamp1}')
        time.sleep(3600)


if __name__ == '__main__':

    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d__UTC%H-%M-%S')
    print(f'Started at {timestamp} ... ')

    night_sleep(12)

    for day in range(7):
        for i in range(12):
            my_scheduler(i)

        night_sleep(12)