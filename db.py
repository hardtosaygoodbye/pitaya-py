import pymysql

connection = pymysql.connect("118.25.210.52","rocky","bw3yGf33x22yjiZt","pitaya")
cursor = connection.cursor(pymysql.cursors.DictCursor)

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
        cursor.execute(sql, args)
        connection.commit()