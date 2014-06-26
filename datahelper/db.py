#!/usr/bin/python
#encoding:utf-8


# author:luyu
# date  :2013-03-26

import sys ,time
import ConfigParser

class DbConfig(object):
	""" DbConfig

		It is the class for load database config
	"""
	dbname  = ''
	configs = {}

	def __init__(self, dbname,configFile='db_config.cfg'):
		self.dbname  = dbname
		# 加载配置文件
		config = ConfigParser.RawConfigParser()
		try:
			config.read(configFile)
			self.configs['type']     = config.get(self.dbname,'type')
			self.configs['host']     = config.get(self.dbname,'host')
			self.configs['username'] = config.get(self.dbname,'username')
			self.configs['password'] = config.get(self.dbname,'password')
			self.configs['encoding'] = config.get(self.dbname,'encoding')
			self.configs['port']     = config.get(self.dbname,'port')
			self.configs['database'] = config.get(self.dbname,'database')
		except Exception, e:
			# 输出日志
			raise e
			exit();

	def getConfig(self):
		return self.configs

		

# 数据库连接简单工厂方法
class ConnectionFactory(object):
	"""ConnectionFactory for different database"""
	dbname = 'default'
	conf   = ''

	def __init__(self, dbname,configFile):
		super(ConnectionFactory, self).__init__()
		self.dbname = dbname
		self.configfile = configFile

	def getConnection(self):
		dbconfig = DbConfig(self.dbname,self.configfile)
		conf     = dbconfig.getConfig()
		self.conf= conf
		dbtype   = conf['type']
		host     = conf['host']
		username = conf['username']
		password = conf['password']
		database = conf['database']
		port     = int(conf['port'])
		encoding = conf['encoding']
		
		if dbtype=='mysql':
			try:
				import MySQLdb
				c = MySQLdb.connect(host,username,password,database,charset=encoding,port=port)
			except Exception, e:
				print e
				raise Exception
		elif dbtype=='oracle':
			try:
				import cx_Oracle
				c = cx_Oracle.connect('%s/%s@%s'%(username,password,database))
			except Exception, e:
				print e
				raise Exception
		elif dbtype=='postgresql' :
			try:
				import psycopg2
				c = psycopg2.connect(host=host,user=username,password=password,port=port,database=database)
			except Exception, e:
				print e
				raise Exception
		elif dbtype=='sqlserver' :
			try:
				import pymssql
				c = pymssql.connect(host=host,user=username,password=password,database=database)
			except Exception, e:
				print e
				raise Exception
	
		return c
	
	
	def getConfig(self):
		return self.conf

		

class Db(object):
	"""DataBase operate class"""

	dbname = 'default'
	conn   = None 
	conf   = ''

	def __init__(self, dbname,configFile='db_config.cfg'):
		super(Db, self).__init__()
		self.dbname = dbname
		dbconn      = ConnectionFactory(self.dbname,configFile)
		self.conn   = dbconn.getConnection()
		self.conf   = dbconn.getConfig()
		
	def getConnection(self):
		return self.conn

	def getConfig(self):
		return self.conf
	
	def getCursor(self):
		return self.conn.cursor()
		
	def execute(self,sql,auto_commit=True):
		# print "[" + time.strftime("%Y-%m-%d %X",time.localtime()) + "]Execute sql is: \n" + sql + "\n"
		cur = self.conn.cursor()
		try:
			cur.execute(sql)
			if auto_commit:
				self.conn.commit()
		except Exception, e:
			self.conn.rollback()
			print e
			raise Exception

	def fetchone(self):
		return self.conn.cursor().fetchone()

	def query(self,sql,fetchall=True):
		# print "[" + time.strftime("%Y-%m-%d %X",time.localtime()) + "]Execute sql is: \n" + sql + "\n"
		cur = self.conn.cursor()
		cur.execute(sql)
		if fetchall:
			alldata = cur.fetchall()
			return alldata
		else:
			return cur

	def executemany(self,sql,val):
		cur = self.conn.cursor()
		try:
			cur.executemany(sql,val)
			self.conn.commit()
		except Exception, e:
			self.conn.rollback()
			print e
			raise Exception

	def commit(self):
		self.conn.commit()
	
	def rollback(self):
		self.conn.rollback()

	def close(self):
		self.conn.close()

	def reConnect(self):
		dbconn      = ConnectionFactory(self.dbname)
		self.conn   = dbconn.getConnection()

