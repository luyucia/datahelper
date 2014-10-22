datahelper
==========

datahelper is an python framework for data developer

- 数据库操作
- 构建sql，插入、更新、批量插入
- 从数据库导出csv，导入csv
- 日期常用操作
- 控制台操作
- 数据库元信息，表名，字段名等



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

def test_meta(self):
    print mt.tables()
    cs = mt.columns('tablename')
    print mt.ddl('tablename')

def test_ip():
    i = datahelper.IpInfo('qqwry.dat')
    ip = i.getAddress('113.111.218.219')
    ip = i.getAddress('173.194.130.4')
    ip = i.getAddress('221.7.8.246')
    ip = i.getAddress('113.194.103.228')
    ip = i.getAddress('222.170.63.27')
    print ip[0]
    print ip[1]
    
def test_ssh():
    shell = datahelper.Ssh('10.0.0.238','root','Tzqg.Kb47')
    shell.scp2('/home/cloud/jobs/job/etl/dwetl/2014-07-01-log_logout.csv','/data/tmp/2014-07-01')

def test_bloomfilter():
    b = datahelper.BloomFilter('url')
    b.set('http://www.cnblogs.com/dolphin0520/archive/2012/11/10/2755089.html')
    b.set('3')
    b.set('luyu3')
    b.set('http://bbs.paris8.org/viewthread.php?tid=6919&page=1')
    print b.get('http://www.cnblogs.com/dolphin0520/archive/2012/11/10/2755089.html')
    print b.get('http://bbs.paris8.org/viewthread.php?tid=6919&page=1')
    print b.get('luyu234233')
    print b.get('luyu2342344')
    print b.get('1')
    print b.get('2')
    print b.get('3')
    print b.get('4')
    print b.get('5')
    
def test_presto():
    db = datahelper.Presto('localhost',8099)
    sql = '''
    select 
    serverid,
    sum(count)
    from 
    op_online_user_dist
    group by serverid
    '''
    data =  db.query(sql)
    for x in data:
        print x[0]

```