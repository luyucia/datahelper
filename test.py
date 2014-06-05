#encoding:utf-8
import datahelper
import datahelper.date as dateutil
import datahelper.console as console

db  = datahelper.Db('data_warehouse')
db2 = datahelper.Db('k25')

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

# test_db()
# test_console()
# test_date()
# test_sql()

# conn = db.getConnection()
# datahelper.csvutil.dbToCsv(conn,'select * from dim_device limit 10','device.csv')

mt = datahelper.Meta(db)

# print mt.tables()
cs = mt.columns('dim_channel')

# print mt.ddl('dim_channel')

for x in cs:
    print x