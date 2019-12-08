import pymongo
import urllib.request
from LuckyNum import *
import time

class myDb:
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost',port=27017)
        #create or connect to jxluckynum database
        self.db = self.client['jxluckynum']
        #connect to TermTable
        self.tterm = self.db['TermTable']
        #if there is no data in TermTable,get data from internet and insert them
        self.createTerm(self.tterm)
        self.tlucky = self.db['LuckyTable']
        self.tinterval = self.db['DataInterval']


    #数据初始化操作，使用过程中无需执行
    def createTerm(self,col):
        if col.count() > 10 :
            print('开奖记录已有数据，不再初始化')
            return;
        else:
            #fill TermTable from network
            termlist = self.getAllTerm()
            print(termlist)
            col.insert(termlist)

    def getAllTerm(self,url="http://www.17500.cn/getData/ssq.TXT"):
        page = urllib.request.urlopen(url)
        html = page.read()
        data = html.decode('utf-8')
        return self.str2term(data)

    def str2term(self, data):
        datas = data.split("\n")
        terms = []
        try:
            for d in datas:
                di = d.split(" ")
                termdata = term()
                termdata.termID = di[0]
                termdata.red = list(map(int,di[2:8]))
                termdata.blue = int(di[8])
                terms.append(termdata.__dict__)
        finally:
            return terms

    def getTermDatas(self,scope):
        datas = self.tterm.find().sort("termID",-1).limit(scope+1)
        result = []
        for data in datas:
            result.append(data)
        result.sort(key=lambda x:x['termID'])
        return result

    def getAllLuckyNum(self):
        luckynums = self.tlucky.find()
        for lucky in luckynums:
            print(lucky)
        return  luckynums


if __name__ == '__main__':
    start = time.clock()
    db = myDb()
    lucky = db.getAllLuckyNum()
    end = time.clock()
    print("数据条数：",lucky.count())
    print("查询所有数据时间为：", end - start)

