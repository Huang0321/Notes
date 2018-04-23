# -*- coding:utf-8 -*-

from redisclass import RedisBase

obj = RedisBase()
msg = 'hello world'
obj.publish_msg(msg)