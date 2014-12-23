#!/usr/bin/python
#encoding:utf-8
# author:luyu
import prestoclient

class Presto(object):
    """docstring for Presto"""
    def __init__(self, host ,port ,catalog='hive',schema='default'):
        super(Presto, self).__init__()
        self.host    = host 
        self.schema  = schema 
        self.port    = port
        self.catalog = catalog
        self.presto = prestoclient.PrestoClient(host,port,catalog)

    def query(self,sql):
        if not self.presto.runquery(sql):
            print "Error: ", self.presto.getlasterrormessage()
        else:
            return self.presto.getdata()
    
    def cleardata(self):
        return self.presto.cleardata()

    def getcolumns(self):
        return self.presto.getcolumns()
    
