#coding:utf-8
# Author:LuYu
# Date:2013-12-31

import datetime
import time
import calendar as cal

def dateOffset(datestr,offset,operate='-'):
	date_diff = datetime.timedelta(days = offset)
	date      = time.strptime(datestr,"%Y-%m-%d")
	startTime = datetime.datetime(date[0], date[1], date[2], date[3], date[4], date[5] )
	if operate=='-':
		return (startTime-date_diff).strftime('%Y-%m-%d')
	else:
		return (startTime+date_diff).strftime('%Y-%m-%d')

def timeOffset(datestr,offset,operate='-'):
	date_diff = datetime.timedelta(seconds = offset)
	date      = datetime.datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S')
	if operate=='-':
		return (date-date_diff).strftime("%Y-%m-%d %H:%M:%S")
	else:
		return (date+date_diff).strftime("%Y-%m-%d %H:%M:%S")

def weekBegin(datestr):
	date   = datetime.datetime.strptime(datestr, '%Y-%m-%d')
	offset =  date.weekday()
	delta=datetime.timedelta(days=offset)
	return str(date-delta)

def weekEnd(datestr):
	date   = datetime.datetime.strptime(datestr, '%Y-%m-%d')
	offset =  6-date.weekday()
	delta=datetime.timedelta(days=offset)
	return str(date+delta)

def monthBegin(datestr):
	date   = datetime.datetime.strptime(datestr, '%Y-%m-%d')
	offset = date.day-1
	delta=datetime.timedelta(days=offset)
	return str(date-delta)
def monthEnd(datestr):
	date   = datetime.datetime.strptime(datestr, '%Y-%m-%d')
	offset = cal.monthrange(date.year, date.month)[1]-date.day
	delta=datetime.timedelta(days=offset)
	return str(date+delta)


if __name__ == '__main__':
	print weekBegin('2014-01-22')
	print weekEnd('2014-01-22')
	print monthBegin('2014-01-22')
	print monthEnd('2014-01-22')
	print timeOffset('2014-01-22 10:50:10',300)
