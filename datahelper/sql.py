#coding:utf-8
import types
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

# 类型转换
def typeChange(value):
	value_type = type(value) 
	if value_type is types.IntType or value_type is types.FloatType:
		return str(value)
	elif value==None:
		return "null"
	elif value_type is types.StringType or value_type is types.UnicodeType:
		return "'%s'"%value.replace("'",'`')
	else:
		return "'%s'"%value

# 构造insert语句，参数为表名及数据行（字典类型）
def insert(table,data):
	columns = []
	values  = []
	for column_name in data:
		columns.append(column_name)
		values.append(typeChange(data[column_name]))
	sql = "insert into %s (%s) values(%s)" % (table,','.join(columns),','.join(values))
	return sql

# def get_batch_insert(table,data):
# 	values  = []
# 	for x in data:
# 		values.append(typeChange(x))
# 	sql = "insert into %s values(%s)"%(table,','.join(values))
# 	return sql

def update(table,data,where):
	values  = []
	for key in data:
		values.append("%s=%s"%(key,typeChange(data[key])))
	sql = "update %s set %s where %s"%(table,','.join(values),where)
	return sql

# 获取批量插入sql
# 样例 s = MultiInsert('test1')
# a.add([0,'luyu'])
# a.add([1,'zhuyinghao'])
# a.getSql()
# class MultiInsert(object):
# 	"""docstring for MultiInsert"""
# 	def __init__(self, table):
# 		super(MultiInsert, self).__init__()
# 		self.table  = table
# 		self.values = ''

# 	def add(self,data):
# 		values  = []
# 		for x in data:
# 			values.append(typeChange(x))
# 		self.values+='('+','.join(values)+"),"

# 	def getSql(self):
# 		if self.values!='':
# 			return "insert into %s values %s"%(self.table,self.values[0:-1])



class BatchInsert(object):
	"""docstring for BatchInsert"""
	def __init__(self, table):
		super(BatchInsert, self).__init__()
		self.table    = table
		# self.values   = ''
		self.values   = []
		self.columns  = []
		self.parsed   = False
		self.sql_head = ''
		self.sql     = []
		self.counts   = 0

	def add(self,data):
		if not self.parsed:
			for key in data:
				self.columns.append(key)
			self.sql_head = "insert into %s (%s) values "%(self.table,','.join(self.columns))
			self.parsed   = True

		values = []

		for colname in self.columns:
			values.append(str(self.def_type(data[colname])))

		self.values.append('('+','.join(values)+")")
		self.counts+=1

	def getColumns(self):
		return self.columns

	def getCount(self):
		return self.counts

	def def_type(self,val):
		if isinstance(val,(int,float)):
			return val
		elif val==None:
			return 'null'
		else:
			return "'%s'"%val

	def clean(self):
		self.values = []


	def getSql(self):
		if self.values!='':
			return self.sql_head+','.join(self.values)



# s = BatchInsert('user')

# for x in xrange(1,100000):
# 	d2 = dict()
# 	d2['name'] = 'luuy2u'
# 	d2['age']  = 102
# 	# d2['id']   = 1
# 	s.add(d2)
# s.getSql()
# print s.getColumns()
# print s.getCounts()


