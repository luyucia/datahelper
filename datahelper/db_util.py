#coding:utf-8
# Author:LuYu
# Date:2013-08-19
import csv
import types
import decimal
import time
import os
import text_util
import re

# 给一个数组（tuple或list）编码，参数为数组，目标编码，源编码（默认utf-8）
def array_encode(arr,enc,source_enc='utf-8'):
	import types
	list = []
	for i in arr:
		if type(i) is types.StringType:
			list.append(i.decode(source_enc).encode(enc))
		else:
			list.append(i)
	return list

mysql_type_map = {
	'int':'int',
	'long':'bigint',
	'float':'double',
	'datetime':'datetime',
	'string':'varchar(255)'
}

# 构建insert语句
def insert_sql(row_list,table_name):
	values = ''
	for x in row_list:
		coltype = type(x)
		if  coltype is types.IntType or coltype is decimal.Decimal or coltype is types.FloatType or coltype is types.LongType:
			values+=str(x)+','
		elif x is None:
			values+="null,"
		else:
			values+="'%s',"%x
	return "insert into %s values(%s)"%(table_name,values.rstrip(','))


def db_to_db(conn_from,conn_to,sql,to_table_name,auto_create=False):
	stime = time.time()
	cur_from = conn_from.cursor()
	cur_to   = conn_to.cursor()
	text_util.color_print("Execute SQL:"+sql,'white')
	print ''
	cur_from.execute(sql)
	row_one  =  cur_from.fetchone()

	if row_one is None:
		text_util.color_print("Nothing to Import [Time Cost:%s s]"%(time.time()-stime),'red')
		print ''
		return False
	# ------------自动建表--------------
	if auto_create:
		colum_names = []
		colum_types = []
		for x in cur_from.description:
		 	colum_names.append(x[0])
		
		for i in row_one:
			coltype = type(i)
			colum_type = 'string'
			if coltype is types.UnicodeType or coltype is types.StringType:
				colum_type = 'string'
			elif coltype is types.IntType or coltype is decimal.Decimal:
				colum_type = 'int'
			elif coltype is types.LongType:
				colum_type = 'long'
			elif coltype is types.FloatType:
				colum_type = 'float'

			pre_date = re.compile('\d{4}-\d{1,2}-\d{1,2}')
			if pre_date.match(str(i)):
				colum_type = 'datetime'

			colum_types.append(colum_type)


		col_num = len(colum_names)
		col_tmp = ''
		for i in range(0,col_num):
			col_tmp+= colum_names[i]+' '+mysql_type_map[colum_types[i]]+','
		ddl_sql =  "create table if not exists %s (%s)" % (to_table_name,col_tmp.rstrip(','))
		print 'DDL sql is :'
		print ddl_sql
		cur_to.execute(ddl_sql) 
	# ------------自动建表结束--------------
	# ------------插入到目标数据库--------------
	print "Import to %s..."%to_table_name
	cur_to.execute(insert_sql(row_one,to_table_name)) 
	while True:
		row = cur_from.fetchone()
		if row==None:
			break
		else:
			cur_to.execute(insert_sql(row,to_table_name))
	# cur_to.close()
	conn_to.commit()
	text_util.color_print("Import Finished! [Time Cost:%s s]"%(time.time()-stime),'green')

