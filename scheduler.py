import subprocess
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BlockingScheduler
from datetime import datetime

id_server = 3999995


def start():
    result = subprocess.run(
        ["twc", "s", "start", f"{id_server}"], capture_output=True, text=True)
    print("Start server", datetime.now())
    print("Result command", result)


def stop():
    result = subprocess.run(
        ["twc", "s", "stop", f"{id_server}"], capture_output=True, text=True)
    print("Stop server", datetime.now())
    print("Result command", result)


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(stop, CronTrigger(hour=0, minute=0))
    scheduler.add_job(start, CronTrigger(hour=8, minute=0))

    scheduler.start()

if __name__ == "__main__":
    main()
