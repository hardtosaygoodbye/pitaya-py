import time

def now():
    return int(time.time())

def one_day():
    return 86400

def today_begin():
    start_time_str = time.strftime('%Y-%m-%d 00:00:00')
    start_time = time.mktime(time.strptime(start_time_str, '%Y-%m-%d %H:%M:%S'))
    return int(start_time)