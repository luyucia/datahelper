#coding:utf-8



    
class MysqlMeta(object):
    """docstring for MysqlMeta"""
    def __init__(self,db):
        super(MysqlMeta, self).__init__()
        self.db   = db
    
    def tables(self):
        return self.db.query("show tables")

    def columns(self,table):
        column = []
        data = self.db.query("show columns from %s"%table)
        for d in data:
            column_dic = {}
            column_dic['name'] = d[0]
            column_dic['type'] = d[1]
            column_dic['null'] = d[2]
            column_dic['default'] = d[4]
            column.append(column_dic)
        return column
    
    def ddl(self,table):
        ddl =  self.db.query("show create table %s"%table)
        return ddl[0][1]

class Meta(object):
    """docstring for Meta"""
    def __init__(self, db):
        super(Meta, self).__init__()
        # self.db   = db
        config    =  db.getConfig()
        self.type = config['type']
        self.meta = MysqlMeta(db)

    # 获取所有表名
    def tables(self):
        return self.meta.tables()
    # 获取字段信息
    def columns(self,table):
        return self.meta.columns(table)
    # 获取DDL语句
    def ddl(self,table):
        return self.meta.ddl(table)

