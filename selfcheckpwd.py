# -*- coding:utf-8 -*-

from pymysql import connect
from redis import Redis
import sys


class ConnRedis(object):

	def __init__(self, name, passwd):
		self._conn = Redis(host='47.106.122.20',
			port=6379,
			password=123456,
			)
		self._name = name
		self._passwd = passwd

	def juge(self):
		r_user = self._conn.hget('user', self._name)
		r_passwd = self._conn.hget('user', self._passwd)
		# user = r_user.decode('utf-8')
		# passwd = byte.decode(r_passwd)
		printt(r_user)
		prin('sb')

obj = ConnRedis('sb', 3332)
obj.juge()

# def conn_redis(name, pwd):
# 	r = Redis(host='47.106.122.20',port=6379, password=123456)
# 	r_user = r.hget('user', 'user')
# 	r_pwd = r.hget('user', 'password')
# 	user = bytes.decode(r_user, 'utf-8')
# 	password = r_pwd.decode('utf-8')
# 	if user == r_user and password = pwd:
# 		return True
# 	else:
# 		return False
	

# def main():
	


# if __name__ == '__main__':
# 	