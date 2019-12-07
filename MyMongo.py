import pymongo
import urllib.request
from calfunc import *
from LuckyNum import *

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


    def createTerm(self,col):
        if col.count() > 10 :
            print('is not here')
            return;
        else:
            #fill TermTable from network
            termlist = self.getAllTerm()
            print(termlist)
            col.insert(termlist)
            for x in col.find():
                print(x)

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
                termdata.red = di[2:8]
                termdata.blue = di[8]
                terms.append(termdata.__dict__)
        finally:
            return terms

    def getTermDatas(self,scope):
        datas = self.tterm.find().sort("termID",-1).limit(scope)
        result = []
        for data in datas:
            result.append(data)
        result.sort(key=lambda x:x['termID'])
        return result


# if __name__ == '__main__':
#     db = myDb()
#     for data in db.getTermDatas(5):
#         print(data['red'],data['blue'])



