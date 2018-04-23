# -*- coding:utf-8 -*-
from redis import Redis
from pymysql import connect
import sys


def con_mysql(sql):
    db = connect(host='47.106.122.20',
        port=3306,
        user='root',
        passwd='123456',
        db='test',
        charset='utf8')

    cursor = db.cursor()
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except:
        return "错误"
    finally:
        db.close()
    return data


def con_redis(name, passwd):

    r = Redis(host='47.106.122.20',        
        port=6379,
        password='123456'
    )
    r_user = r.hget('user', 'user')
    r_pwd = r.hget('user', 'password')
    user = r_user.decode('utf-8')
    password = r_pwd.decode('utf-8')
    if name == user and password == passwd:
        return True
    else:
    	return False

    
if __name__ == '__main__':
    #获取传入的姓名和密码参数
    name = sys.argv[1]
    passwd = sys.argv[2]
    # 传入的redis中，进行校验        
    if not con_redis(name, passwd):
        sql = "select * from users where u_name='%s' and passwords='%s'" % (name, passwd)
        data = con_mysql(sql)
        if data:
            r = Redis(host='47.106.122.20',
                port=6379,
                password='123456')
            r.hset('user', 'user', name)
            r.hset('user', 'password', passwd)
            print('mysql中数据正确,登录成功')
        else:
            print('数据库中数据不正确,登录不成功')
    else:
        print('redis中数据正确,登录成功')



