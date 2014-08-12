#!/usr/bin/python
#encoding:utf-8


# author:luyu
# date  :2014-08-12
import redis
import ConfigParser
class BloomFilter(object):
    configs = {}

    def __init__(self, name):
        super(BloomFilter, self).__init__()
        self.name  = name
        self.seeds = [3,7,11,13,31,37,61]
        # 加载配置文件
        config = ConfigParser.RawConfigParser()
        try:
            config.read('config/redis_config.cfg')
            self.configs['host']     = config.get('bloomfilter','host')
            self.configs['password'] = config.get('bloomfilter','password')
            self.configs['port']     = int(config.get('bloomfilter','port'))
            self.configs['database'] = config.get('bloomfilter','database')
        except Exception, e:
            # 输出日志
            raise e
            exit();
        self.r     = redis.StrictRedis(self.configs['host'], self.configs['port'], self.configs['database'] , self.configs['password'])
    def getHashValue(self,string,n):
        result = 0
        for s in string:
            result = self.seeds[n]*result+ ord(s)
            if result > 2<<24:
                result%=2<<24
        return result

    def bitset(self,name,offset,value=1):
        self.r.setbit('rep:'+name,offset,value)

    def bitget(self,name,offset):
        return self.r.getbit('rep:'+name,offset)

    def set(self,string):
        for i in xrange(0,7):
            hashpos = self.getHashValue(string,i)
            self.bitset(self.name,hashpos)

    def get(self,string):
        for i in xrange(0,7):
            hashpos = self.getHashValue(string,i)
            if self.bitget(self.name,hashpos) == 0 :
                return False
        return True