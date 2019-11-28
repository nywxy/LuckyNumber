from dataoption import dbase

db = dbase()

db.dbOptionWithSql("select * from TermTable where term>2019000")
print(db.cursor.fetchall())
