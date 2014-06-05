#coding:utf-8
# Author:LuYu
# Date:2013-08-19
import csv
import types
import decimal
import time
import os

# 给一个数组（tuple或list）编码，参数为数组，目标编码，源编码（默认utf-8）
def arrayEncode(arr,enc,source_enc='utf-8'):
	import types
	list = []
	for i in arr:
		if type(i) is types.StringType:
			list.append(i.decode(source_enc).encode(enc))
		else:
			list.append(i)
	return list

# 数据库->CSV文件，参数为数据库连接、sql语句、csv文件名，表头(可选，逗号分隔，默认不填即表头)
def dbToCsv(conn,sql,file_path,title=''):
	stime = time.time()
	writer  =  csv.writer(file(file_path,'wb'))
	c       =  conn.cursor()
	c.execute(sql)
	print 'Run Sql-->'+sql
	if title!='':
		writer.writerow(arrayEncode(title.split(','),'gb18030'))
	while True:
		row = c.fetchone()
		if not row:break
		writer.writerow(arrayEncode(row,'gb18030'))
	print 'Export to '+os.path.abspath(file_path)+' Finished![Time Cost:%s s]'%(time.time()-stime)

# CSV文件->数据库，参数为文件名，连接，表名
def csvToDb(filename,conn,table):
	with open(filename,'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(1024))
		csvfile.seek(0)
		reader = csv.reader(csvfile,dialect)
		for row in reader:
			values = ''
			for i in row:
				if type(i) is str:
					values+="'%s',"%i
				else:
					values+="%s,"%str(i)
			sql = "insert into "+table+" values("+values.rstrip(',')+")"
			conn.execute(sql.decode('gb18030').encode('utf-8'))
		conn.commit()

# 读取csv文件的某列，到列表中
def load_column(filename,col_num=0):
	col_list = []
	with open(filename,'rb') as csvfile:
		dialect = csv.Sniffer().sniff(csvfile.read(1024))
		csvfile.seek(0)
		reader = csv.reader(csvfile,dialect)
		for row in reader:
			col_list.append(row[col_num])
		return col_list

def csv_to_mem(dic_name,filename,pkey,sep=","):
	print 'Loading '+filename+'.'
	dic_crkmx  = {}
	line_count = 0;
	fp = open(filename,'r')
	if pkey==-1:
		try:
			while True:
				line = fp.readline()
				if not line:
					break
				t =  line.rstrip().split(sep)
				dic_name[line_count] = t
				line_count=line_count+1
		finally:
			fp.close()
	else:
		try:
			while True:
				line = fp.readline()
				if not line:
					break
				t =  line.rstrip().split(sep)
				dic_name[t[pkey]] = t
				line_count=line_count+1
		finally:
			fp.close()


def mem_to_csv():
	pass
def mem_to_db():
	pass
def db_to_mem():
	pass

mysql_type_map = {
	'int':'int',
	'long':'bigint',
	'float':'double',
	'string':'varchar(255)'
}

# 构建insert语句
def insert_sql(row_list,table_name):
	values = ''
	for x in row_list:
		if type(x) is types.UnicodeType:
			values+="'%s',"%x
		else:
			values+=str(x)+','
	return "insert into %s values(%s)"%(table_name,values.rstrip(','))


def db_to_db(conn_from,conn_to,sql,to_table_name):
	stime = time.time()
	cur_from = conn_from.cursor()
	cur_to   = conn_to.cursor()
	cur_from.execute(sql)

	colum_names = []
	colum_types = []
	for x in cur_from.description:
	 	colum_names.append(x[0])
	
	row_one =  cur_from.fetchone()
	for i in row_one:
		coltype = type(i)
		if coltype is types.UnicodeType or coltype is types.StringType:
			colum_types.append('string')
		elif coltype is types.IntType or coltype is decimal.Decimal:
			colum_types.append('int')
		elif coltype is types.LongType:
			colum_types.append('long')
		elif coltype is types.FloatType:
			colum_types.append('float')
		else:
			colum_types.append('string')

	# print colum_names
	# print colum_types
	col_num = len(colum_names)
	col_tmp = ''
	for i in range(0,col_num):
		col_tmp+= colum_names[i]+' '+mysql_type_map[colum_types[i]]+','

	ddl_sql =  "create table if not exists %s (%s)" % (to_table_name,col_tmp.rstrip(','))
	
	print 'DDL sql is :'
	print ddl_sql
	print "Import to %s..."%to_table_name
	cur_to.execute(ddl_sql) 
	cur_to.execute(insert_sql(row_one,to_table_name)) 
	while True:
		row = cur_from.fetchone()
		if row==None:
			break
		else:
			cur_to.execute(insert_sql(row,to_table_name))
	cur_to.close()
	conn_to.commit()
	print "Import Finished! [Time Cost:%s s]"%(time.time()-stime)

# conn1 = sqlite3.connect('test3.db')
# conn2 = sqlite3.connect('test2.db')
# conn = sqlite3.connect('duomi.db')
# c = conn1.cursor()
# c.execute('create table if not exists test2(id integer,name varchar(100),score float,age date )')
# c.execute("insert into test2 values(1,'ssdfd',0.5,'2013-02-01')")
# c.execute("insert into test2 values(2,'ssfghwdfd',0.5,'2013-02-01')")
# c.execute("insert into test2 values(3,'jfgh',0.5,'2013-02-01')")
# c.execute("insert into test2 values(4,'ssdfdgdfd',0.5,'2013-02-01')")
# c.execute("insert into test2 values(5,'sreedfd',0.5,'2013-02-01')")
# c.execute("insert into test2 values(6,'ssdfd',0.5,'2013-02-01')")
# c.close()
# conn1.commit()

# db_to_db(conn1,conn2,"select * from tmp_bug",'test4')

# dbToCsv(conn1,"select * from tmp_bug",'export.csv')
# c = conn.cursor()
# c.execute('create table choujiang (ip varchar(20),date varchar(20),times int)')
# csvToDb('duomi.csv',conn,'choujiang')