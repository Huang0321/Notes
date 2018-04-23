# -*- coding:utf-8 -*-


import redis

class RedisBase(object):

    def __init__(self):
        self._conn = redis.Redis(host='47.106.122.20', port=6379, password='123456')
        self.channel = 'test'
    
    # 发布
    def publish_msg(self, msg):
        self._conn.publish(self.channel, msg)
    
    # 订阅
    def subscribe_msg(self):
        pub = self._conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub
      

