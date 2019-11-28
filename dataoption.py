import sqlite3

class dbase:

    def __init__(self):
        # 连接数据库
        self.conn = sqlite3.connect("data/number.db")
        # 创建一个游标cursor
        self.cursor = self.conn.cursor()

    def getAllData(self,tablename):
        if self.cursor:
            self.cursor.execute("select * from %s" %tablename)
            values = self.cursor.fetchall()
            return values

    def getDataByCondition(self,tablename,condition):
        if self.cursor:
            self.cursor.execute("select * from %s %s" % tablename,condition)
            values = self.cursor.fetchall()
            return values

    def dbOptionWithSql(self,sql):
        if self.cursor:
            self.cursor.execute(sql)