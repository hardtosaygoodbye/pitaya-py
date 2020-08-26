import db
import requests
import time

# 查找日线数据
def select_one_day(from_t, to_t):
    res = db.select('select * from one_day where ts between %s and %s;', (from_t, to_t))
    return res

# 更改日线数据
def update_one_day(t, o, c, h, l):
    db.execute('''
        UPDATE one_day SET open_price = %s, close_price = %s, high_price = %s, low_price = %s WHERE ts = %s
    ''', (o, c, h, l, t))

# 增加日线数据
def insert_one_day(t, o, c, h, l):
    db.execute('''
        INSERT INTO one_day (ts, open_price, close_price, high_price, low_price) VALUES (%s, %s, %s, %s, %s)
    ''', (t, o, c, h, l))

# 获取网络最新日线数据
# TODO: 这里from_t不太对，看看应该取值多少比较合理, 拿到的时间戳有偏差，在这一层就弄干净，去遍历t改掉
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
    res = db.select('select * from half_hour where ts between %s and %s;', (from_t, to_t))
    return res

# 更改半小时数据
def update_half_hour(t,o,c,h,l):
    db.execute('''
        UPDATE half_hour SET open_price = %s, close_price = %s, high_price = %s, low_price = %s WHERE ts = %s
    ''',(o, c, h, l, t))

# 增加半小时数据
def insert_half_hour(t,o,c,h,l):
    db.execute('''
        INSERT INTO half_hour (ts, open_price, close_price, high_price, low_price) VALUES (%s, %s, %s, %s, %s)
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

# 想验证代码，直接python dao.py就会执行到这里，不用特地写个接口
# dao层所有时间参数都用时间戳
# 数据库字段和别人数据库保持一致吧，否则也容易乱掉，直接t,o,c,h,l五个字段，写变量名的时候也好写，new_t, tmp_t, xxx_o
if __name__ == '__main__':
    request_latest_one_day()