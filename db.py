import pymysql
import threading

connection = pymysql.connect("118.25.210.52","rocky","bw3yGf33x22yjiZt","pitaya")
cursor = connection.cursor(pymysql.cursors.DictCursor)
lock = threading.Lock()

# 查询
def select(sql, args=None):
    cursor.execute(sql, args)
    return cursor.fetchall()

# 增删改
def execute(sql, args=None):
    if type(args) is list:
        cursor.executemany(sql, args)
        connection.commit()
    elif type(args) is tuple or type(args) is None:
        lock.acquire()
        cursor.execute(sql, args)
        lock.release()
        connection.commit()