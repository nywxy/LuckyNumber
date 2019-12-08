import pymongo
import urllib.request
from LuckyNum import *
import time
import time

class myDb:
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost',port=27017)
        #create or connect to jxluckynum database
        self.db = self.client['jxluckynum']
        #connect to TermTable
        self.tterm = self.db['TermTable']
        #if there is no data in TermTable,get data from internet and insert them
        self.tlucky = self.db['LuckyTable']
        self.tinterval = self.db['DataInterval']

        self.__updateInfo = []

    def getUpdateInfo(self):
        return self.__updateInfo

    #创建或更新开奖记录表
    def createOrUpdateTermTable(self):
        #首先从网络上下载最新的开奖信息表
        termlist = self.__getAllTerm()
        #然后看数据库中是否有数据，
        #没有数据的话就创建表并填充数据
        if self.tterm.count() == 0 :
            print('正在生成开奖信息表........')
            start = time.clock()
            self.tterm.insert(termlist)
            end = time.clock()
            print('生成开奖信息数据完毕，用时:',end-start)
        else:
            #已经生成过开奖数据的话，就根据数据库中的最后一条数据与下载的最新数据进行比对，如果期数一致
            #则退出，否则就提示更新，并自动进行更新

    #创建开奖记录表
    def createTerm(self):
        if self.tterm.count() > 10 :
            print('开奖记录已有数据，不再初始化')
            return
        else:
            #fill TermTable from network
            termlist = self.__getAllTerm()
            self.tterm.insert(termlist)

    def __getAllTerm(self,url="http://www.17500.cn/getData/ssq.TXT"):
        page = urllib.request.urlopen(url)
        html = page.read()
        data = html.decode('utf-8')
        return self.__str2term(data)

    def __str2term(self, data):
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
        return luckynums

    def getAllDataInterval(self):
        return self.tinterval.find().sort('dataID')


