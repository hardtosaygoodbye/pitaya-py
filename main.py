from flask import Flask
import db
import requests
import time
import datetime
app = Flask(__name__)

@app.route('/hello')
def hello():
    res = db.execute("select * from one_day")
    return {
        'code': 0,
        'msg': 'success',
        'data': res,
    }

@app.route('/gettodayhalfhour')
def gettodayhalfhour():
    date = datetime.date.today()
    date = date.strftime("%Y-%m-%d")
    timeArray = time.strptime(date, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))
    sql_sentance = "SELECT * FROM half_hour_test where ts >= "
    timeStamp = str(timeStamp)
    # 是不是不能这么写
    sql_sentance = sql_sentance + timeStamp
    gold_price_database = db.execute(sql_sentance)

    return {
        'code': 0,
        'msg': 'success',
        'data': gold_price_database,
    }

@app.route('/getdata')
def get_data():
    get_start_time = int(time.time()) - 604800
    get_end_time = int(time.time())
    gold_price_request = requests.get(
        'https://tradingview.2rich.net/TradingInterface/history/',
        headers = {'Referer': '1'},
        params = {
            'symbol':'FEAUUS',
            'resolution': '1d',
            'from': get_start_time,
            'to': get_end_time
        }
    )
    gold_price_response = gold_price_request.json()
    sql_sentance = "SELECT * FROM one_day_test where ts >= "
    data_get_time = str(get_start_time)
    # 是不是不能这么写
    sql_sentance = sql_sentance + data_get_time
    gold_price_database = db.execute(sql_sentance)
    price_ts_new = gold_price_response.get("t")
    price_open_new = gold_price_response.get("o")
    price_close_new = gold_price_response.get("c")
    price_high_new = gold_price_response.get("h")
    price_low_new = gold_price_response.get("l")
    different_index = list()
    price_ts_new_list = list()
    for price_ts in gold_price_database :
        price_ts_new_list.append(price_ts.get("ts"))

    if not gold_price_database :
     insert_sql = "INSERT INTO one_day_test(ts, open_price, close_price, high_price, low_price,check_time) VALUES (%s, %s, %s, %s, %s, %s)"
     insert_list = []
     for i in range(len(price_ts_new)) :  
      price_check_time_new = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(price_ts_new[i]-28800))
      insert_element = (price_ts_new[i]-28800,price_open_new[i],price_close_new[i],price_high_new[i],price_low_new[i],price_check_time)
      insert_list.append(insert_element)
     cursor = db.executeDay(insert_sql,insert_list) 
    else :
     for old in gold_price_database :       
      for new_index in range(len(price_ts_new)) :
        if (price_ts_new[new_index]-28800) not in price_ts_new_list :
            insert_sql = "INSERT INTO one_day_test(ts, open_price, close_price, high_price, low_price,check_time) VALUES (%s, %s, %s, %s, %s, %s)"
            price_check_time_new = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(price_ts_new[new_index]-28800))
            insert_list = (price_ts_new[new_index]-28800,price_open_new[new_index],price_close_new[new_index],price_high_new[new_index],price_low_new[new_index],price_check_time_new)
            cursor = db.execute_one(insert_sql,insert_list) 
            break
        if old.get("ts") == price_ts_new[new_index]-28800:
            if float(old.get("open_price")) != price_open_new[new_index] or float(old.get("close_price")) != price_close_new[new_index] or float(old.get("high_price")) != price_high_new[new_index] or float(old.get("low_price")) != price_low_new[new_index] :
                different_index.append(new_index)
                break
            break
     for insert_index in different_index :
         insert_sql_different = "UPDATE one_day_test SET open_price = %s, close_price = %s, high_price = %s, low_price = %s, check_time = %s WHERE ts = %s"
         price_check_time_new = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(price_ts_new[insert_index]-28800))
         insert_list_different = (price_open_new[insert_index],price_close_new[insert_index],price_high_new[insert_index],price_low_new[insert_index],price_check_time_new,price_ts_new[insert_index]-28800)
         cursor = db.execute_one(insert_sql_different,insert_list_different) 
     
    return "ok"

if __name__ == '__main__':
    app.run()