from flask import Flask
import dao
import ts
app = Flask(__name__)

@app.route('/hello')
def hello():
    return {
        'code': 0,
        'msg': 'hello success'
    }

# 日线数据更新
@app.route('/update_one_day')
def update_one_day():
    net_data = dao.request_latest_one_day()
    db_data = dao.select_one_day(ts.now() - ts.one_day() * 7, ts.now())
    for i in range(len(net_data['t'])):
        is_new_data = True
        for one_db_data in db_data:
            if net_data['t'][i]== one_db_data['ts']:
                is_new_data = False
                dao.update_one_day(net_data['t'][i], net_data['o'][i], net_data['c'][i], net_data['h'][i], net_data['l'][i])
            else:
                continue
        if is_new_data:
            dao.insert_one_day(net_data['t'][i], net_data['o'][i], net_data['c'][i], net_data['h'][i], net_data['l'][i])
    return {
        'code': 0,
        'msg': 'update success'
    }

# 半小时数据更新


if __name__ == '__main__':
    app.run()