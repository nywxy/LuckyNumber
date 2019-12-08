from MyMongo import *
from calfunc import *
from LuckyNum import *
import time
import threading

class calModule():
    __modb = myDb()
    def __init__(self,page):
        self.termData = []
        self.termDataUnkonw = luckyNum()
        self.__pageID = page

    def __getTermDataRight(self,data):
        res = []
        for d in data:
            res.append(Right(d))
        return res

    #数据库初始化为空时才执行此函数，一般就调用一次
    def fillTermData(self,scope):
        datas = self.__modb.getTermDatas(scope)
        if self.__pageID > 1 and self.__pageID < 34:
            for data in datas:
                for index in range(len(data['red'])):
                    data['red'][index] += self.__pageID
                    if data['red'][index] > 33:
                        data['red'][index] -= 33

        for index in range(len(datas)):
            if index > 1:
                pageData = self.__groupCal(self.__pageID,1,216,datas[index],datas[index-1])
                if len(pageData)>0:
                    self.__modb.tlucky.insert(pageData)


    #termdata应该为本期未开奖的数据
    #resultdata为上期开奖结果
    #私有方法，类外不可调用
    def __groupCal(self,page,funcStart,funcEnd,termdata,resultdata):
        pageData = []
        groupNum = int(funcEnd / 6)
        termRightData = self.__getTermDataRight(resultdata['red'])
        onePageNum = self.__calFuncByGroup(funcStart, funcEnd, resultdata['red'], resultdata['blue'])
        # 开奖号码尾数去重
        termRightData = list(set(termRightData))
        for g in range(groupNum):
            #概率性数据集表
            calRes = luckyNum()
            calRes.moduleID = page
            calRes.termID = termdata['termID']
            calRes.groupID = g+1
            calRes.dataID = calRes.termID+'{:0>3d}{:0>3d}'.format(calRes.moduleID,calRes.groupID)
            calRes.num = onePageNum[g * 6:(g + 1) * 6]
            calRes.numSize = len(list(set(calRes.num)))
            calRes.rightNum = 0
            for val in termRightData:
                if val in list(set(calRes.num)):
                    calRes.rightNum += 1
            pageData.append(calRes.__dict__)
            #数据概率周期表
            if calRes.numSize >= 5 and (calRes.rightNum >=5 or calRes.rightNum ==0):
                dataIn = dataInterval()
                dataIn.dataID = calRes.dataID
                dataIn.numSize = calRes.numSize
                dataIn.rightNum = calRes.rightNum
                self.__modb.tinterval.insert(dataIn.__dict__)
        return pageData


    def __calFuncByGroup(self,funcStart,funcEnd,red,blue):
        result = []
        for x in range(funcStart,funcEnd+1):
            result.append(eval("jxM%d"%x)(red,blue))
        return result

lock = threading.Lock()

def fillOnePage(page):
    lock.acquire()
    try:
        calmod = calModule(page + 1)
        calmod.fillTermData(100)
    finally:
        lock.release()

if __name__ == '__main__':
    start = time.clock()
    for page in range(34):
        T1 = threading.Thread(target=fillOnePage,args=(page,))
        T1.start()
        T1.join()
    end = time.clock()
    print("计算时间为：",end-start)
