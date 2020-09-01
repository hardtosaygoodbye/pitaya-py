import db
import requests
import time

# 查找日线数据
def select_one_day(from_t, to_t):
    res = db.select('select * from one_day where t between %s and %s;', (from_t, to_t))
    return res

# 更改日线数据
def update_one_day(t, o, c, h, l):
    db.execute('''
        UPDATE one_day SET o = %s, c = %s, h = %s, l = %s WHERE t = %s
    ''', (o, c, h, l, t))

# 增加日线数据
def insert_one_day(t, o, c, h, l):
    db.execute('''
        INSERT INTO one_day (t, o, c, h, l) VALUES (%s, %s, %s, %s, %s)
    ''', (t, o, c, h, l))

# 获取网络最新日线数据
def request_latest_one_day():
    from_t = int(time.time()) - 604800
    to_t = int(time.time())
    res = requests.get(
        'https://tradingview.2rich.net/TradingInterface/history/',
        headers = {'Referer': '1'},
        params = {
            'symbol':'FEAUUS',
            'resolution': '1d',
            'from': from_t,
            'to': to_t
        }
    ).json()
    return correct_time_stamp(res)

# 查找半小时数据
def select_half_hour(from_t, to_t):
    res = db.select('select * from half_hour where t between %s and %s;', (from_t, to_t))
    return res

# 更改半小时数据
def update_half_hour(t,o,c,h,l):
    db.execute('''
        UPDATE half_hour SET o = %s, c = %s, h = %s, l = %s WHERE t = %s
    ''',(o, c, h, l, t))

# 增加半小时数据
def insert_half_hour(t,o,c,h,l):
    db.execute('''
        INSERT INTO half_hour (t, o, c, h, l) VALUES (%s, %s, %s, %s, %s)
    ''',(t, o, c, h, l))

# 获取网络最新半小时数据
def request_latest_half_hour():
    from_t = int(time.time()) - 259200
    to_t = int(time.time())
    res = requests.get(
        'https://tradingview.2rich.net/TradingInterface/history/',
        headers = {'Referer': '1'},
        params = {
            'symbol':'FEAUUS',
            'resolution': '30',
            'from': from_t,
            'to': to_t
        }
    ).json()
    return correct_time_stamp(res)

# 处理时间戳偏差
def correct_time_stamp(net_data):
    for i in range(len(net_data['t'])) :
        net_data['t'][i] = net_data['t'][i] - 28800
    return net_data    

# 获取当前时间戳所在一天的半小时数据



if __name__ == '__main__':
    request_latest_one_day()