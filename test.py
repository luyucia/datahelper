#encoding:utf-8
import datahelper
import datahelper.date as dateutil
import datahelper.console as console

db  = datahelper.Db('data_warehouse','/home/cloud/jobs/job/day/db_config.cfg')
db2 = datahelper.Db('k25','/home/cloud/jobs/job/day/db_config.cfg')

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
    print dateutil.dateOffset('2014-05-09',1)
    print dateutil.dateOffset('2014-05-09',-1)
    print dateutil.timeOffset('2014-01-22 10:50:10',300)
    print dateutil.timeOffset('2014-01-22 10:50:10',-300)
    print dateutil.weekBegin('2014-01-22')
    print dateutil.weekEnd('2014-01-22')
    print dateutil.monthBegin('2014-01-22')
    print dateutil.monthEnd('2014-01-22')

def test_console():
    console.colorPrint('wrong')
    console.colorPrint('wrong')
    console.colorPrintln('wrong','green')
    console.colorPrintln('wrong')

def test_sql():
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

def test_ip():
    i = datahelper.IpInfo('qqwry.dat')
    ip = i.getAddress('113.111.218.219')
    ip = i.getAddress('173.194.130.4')
    ip = i.getAddress('221.7.8.246')
    ip = i.getAddress('113.194.103.228')
    ip = i.getAddress('222.170.63.27')
    print i.getProvince('113.111.218.219')
    print i.getProvince('222.170.63.27')
    print i.getProvince('221.7.8.246')
    print ip[0]
    print ip[1]

def test_ssh():
    shell = datahelper.Ssh('10.0.0.xxxx','root','xxxxxx')
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


def testEmailHelper():
    e = datahelper.EmailHelper('luyu@kingsoft.com','bjmail.kingsoft.com','luyu','pxxxxxx')
    e.setContent("test","<h1>你好</h1>")
    e.addAttach("README.rst",'测试文件.txt')
    e.addAttach("README.rst",'测试文件2.txt')
    e.send('luyu@kingsoft.com')

def testPresto():
    p = datahelper.Presto('10.0.2.11',8099)
    sql='''show tables'''
    print p.query(sql)
    
# test_db()
# test_console()
# test_date()
# test_sql()
# test_ip()
testEmailHelper()

# conn = db.getConnection()
# datahelper.csvutil.dbToCsv(conn,'select * from dim_device limit 10','device.csv')

# mt = datahelper.Meta(db)

# print mt.tables()
# cs = mt.columns('dim_channel')

# print mt.ddl('dim_channel')

# for x in cs:
#     print x
# import redis
# r  = redis.StrictRedis(host='127.0.0.1', port=6379, db=8 , password='6KGz$1mub')

# r.setbit('rep:user',1000000000,1)
# print r.getbit('rep:user',10000)
# r.delete('rep:user')