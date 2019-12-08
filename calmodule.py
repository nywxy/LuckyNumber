from MyMongo import *
from calfunc import *
from LuckyNum import *
import time
import threading

class calModule():
    __modb = myDb()
    def __init__(self):
        self.termData = []
        self.termDataUnkonw = luckyNum()

        self.__page = 0   #生成多少页数据
        self.__scope = 0  #生成多少期数据
        self.__intervalThreshold = 10 #查找间隔阈值

    def getIntervalThreshold(self):
        return self.__intervalThreshold

    def getPageCount(self):
        return self.__page

    def getScope(self):
        return self.__scope

    def setIntervalThreshold(self,val):
        self.__intervalThreshold = val

    def setPageCount(self,val):
        self.__page = val

    def setScope(self,val):
        self.__scope = val

    #初始化数据库，包括生成开奖信息表，概率计算表和初始化概算数据间隔表
    def initData(self,page,scope):
        self.__page = page
        self.__scope = scope

        #首先生成TermTable中的数据


    def __getTermDataRight(self,data):
        res = []
        for d in data:
            res.append(Right(d))
        return res

    #数据库初始化为空时才执行此函数，一般就调用一次
    def __fillTermData(self,scope,page):
        datas = self.__modb.getTermDatas(scope)
        if page > 1 and page < 34:
            for data in datas:
                for index in range(len(data['red'])):
                    data['red'][index] += page
                    if data['red'][index] > 33:
                        data['red'][index] -= 33

        for index in range(len(datas)):
            if index > 1:
                pageData = self.__groupCal(page,1,216,datas[index],datas[index-1])
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
                dataIn.termID = calRes.termID
                dataIn.moduleID = calRes.moduleID
                dataIn.groupID = calRes.groupID
                dataIn.numSize = calRes.numSize
                dataIn.rightNum = calRes.rightNum
                self.__modb.tinterval.insert(dataIn.__dict__)
        return pageData

    @classmethod
    def getAllDataInterval(cls):
        return cls.__modb.getAllDataInterval()

    @classmethod
    def updateInterval(cls,dataIn):
        datas = cls.__modb.tinterval.find({'moduleID':dataIn['moduleID'],
                                             'groupID':dataIn['groupID'],
                                             'numSize':dataIn['numSize'],
                                             'rightNum':dataIn['rightNum']}).sort('dataID')
        if datas.count() > 0:
            mod = []
            for data in datas:
                mod.append(data)
            #计算周期间隔
            #最早一个数据的周期间隔不计算，为9999
            for index in range(len(mod)):
                if mod[index]['last66']!=-1 or mod[index]['last65']!=-1 or mod[index]['last60']!=-1 or  mod[index]['last55'] != -1 or mod[index]['last50']!=-1 :
                    print('-------------------------------------')
                    continue
                else:
                    if index == 0:
                        mod[index]['last%d%d'%(mod[index]['numSize'],mod[index]['rightNum'])] = 9999
                    elif index > 0:
                        mod[index]['last%d%d' % (mod[index]['numSize'],mod[index]['rightNum'])] = \
                            int(mod[index]['termID']) - int(mod[index-1]['termID'])

                    cls.__modb.tinterval.update({'dataID':mod[index]['dataID']},
                                                {'$set':{'last%d%d'%(mod[index]['numSize'],
                                                         mod[index]['rightNum']):mod[index]['last%d%d' % (
                                                         mod[index]['numSize'], mod[index]['rightNum'])]}})

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
        # calmod.fillTermData(200)
    finally:
        lock.release()

if __name__ == '__main__':
    start = time.clock()
    for page in range(34):
        T1 = threading.Thread(target=fillOnePage,args=(page,))
        T1.start()
        T1.join()
    for x in calModule.getAllDataInterval():
        calModule.updateInterval(x)
    end = time.clock()
    print("计算时间为：",end-start)

