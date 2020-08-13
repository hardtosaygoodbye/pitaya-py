from flask import Flask
import db
app = Flask(__name__)

@app.route('/hello')
def hello():
    res = db.execute("select * from one_day")
    return {
        'code': 0,
        'msg': 'success',
        'data': res,
    }

if __name__ == '__main__':
    app.run()