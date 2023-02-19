import datetime
import schedule


def print_ky():
    t = datetime.datetime.now()
    t = t.hour % 12
    print("ку " * int(t))


schedule.every().hour.at(":00").do(print_ky())

while True:
    schedule.run_pending()
