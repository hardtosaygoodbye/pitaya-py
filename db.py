import pymysql

db = pymysql.connect("118.25.210.52","rocky","bw3yGf33x22yjiZt","pitaya")
cursor = db.cursor(pymysql.cursors.DictCursor)

def execute(sql):
    cursor.execute(sql)
    return cursor.fetchall()

def executeDay(sql,args_list):
    cursor.executemany(sql,args_list)
    db.commit()
    return True
    
def execute_one(sql,value):
    cursor.execute(sql,value)
    db.commit()
    return True  