datahelper
==========

datahelper is an python framework for data developer

```python
#encoding:utf-8
import datahelper
import datahelper.date as dateutil
import datahelper.console as console

db  = datahelper.Db('data_warehouse','db_config.ini')

def test_db():
    # 迭代查询
    c  =  db.query("select * from dim_game",False)
    while True:
        d = c.fetchone()
        if not d:
            break
        print d

    # 全量查询
    data  =  db.query("select * from dim_game")
    print data

    # 查询配置信息
    print db.getConfig()

def test_date():
    # 获取前一天
    print dateutil.dateOffset('2014-05-09',1)
    # 获取后一天
    print dateutil.dateOffset('2014-05-09',-1)
    # 时间向前偏移300秒
    print dateutil.timeOffset('2014-01-22 10:50:10',300)
    # 时间向后偏移300秒
    print dateutil.timeOffset('2014-01-22 10:50:10',-300)
    # 获取一周开始时的日期
    print dateutil.weekBegin('2014-01-22')
    # 获取周末的日期
    print dateutil.weekEnd('2014-01-22')
    # 获取月初日期
    print dateutil.monthBegin('2014-01-22')
    # 获取月末日期
    print dateutil.monthEnd('2014-01-22')

def test_console():
    # 带颜色的终端输出
    console.colorPrint('wrong')
    console.colorPrint('wrong')
    console.colorPrintln('wrong','green')
    console.colorPrintln('wrong')

def test_sql():
    # 构造批量插入sql，
    s  =  datahelper.sql.BatchInsert('test')
    for x in xrange(1,10):
      d2 = dict()
      d2['name'] = 'luuy2u'
      d2['age']  = 102
      # d2['id']   = 1
      s.add(d2)
    print s.getSql()
    print s.getColumns()
    print s.getCount()

def test_csv():
    conn = db.getConnection()
    # 根据sql导出csv，参数为数据库连接，sql语句，文件名，表头（可选 格式为逗号分隔的字符串）
    datahelper.csvutil.dbToCsv(conn,'select * from dim_device limit 10','device.csv')

```