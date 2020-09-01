import time
import datetime

def now():
    return int(time.time())

def one_day():
    return 86400

def ts2time(ts):
    time_arr = time.localtime(ts)
    return time.strftime("%Y--%m--%d %H:%M:%S", time_arr)

def ts2date(ts):
    time_arr = time.localtime(ts)
    return time.strftime("%Y-%m-%d", time_arr)

def ts_in_day_range(ts):
    tmp = time.localtime(ts)
    start_ts = time.mktime(time.struct_time((tmp.tm_year, tmp.tm_mon, tmp.tm_mday, 6, 0, 0, 0, 0, 0)))
    end_ts = time.mktime(time.struct_time((tmp.tm_year, tmp.tm_mon, tmp.tm_mday, 6, 0, 0, 0, 0, 0)))
    return [start_ts, end_ts]

if __name__ == '__main__':
    res = ts_in_day_range(1262534400)
    print(res)