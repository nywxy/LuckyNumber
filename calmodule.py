from MyMongo import *
from calfunc import *
from LuckyNum import *
import time
import threading

class calModule():
    __modb = myDb()
    def __init__(self):
        self.updateTermData = []
        self.isUpdate = False
        self.__page = 33   #生成多少页数据
        self.__scope = 100  #生成多少期数据
        self.__zone = 32
        self.__intervalThreshold = 10 #查找间隔阈值
        self.__funcStart = 1 #计算函数开始索引
        self.__funcEnd = 216 #计算函数结束索引
        self.termForcast = ""

    #---------------对外接口--------------------------

    #获取设定的查阈值
    def getIntervalThreshold(self):
        return self.__intervalThreshold

    #获取生成多少页
    def getPageCount(self):
        return self.__page

    #获取生成多少期的数据
    def getScope(self):
        return self.__scope

    #获取设置的函数开始索引
    def getFuncStart(self):
        return self.__funcStart

    #获取设置的函数结束索引
    def getFuncEnd(self):
        return self.__funcEnd

    #设置查找的阈值
    def setIntervalThreshold(self,val):
        self.__intervalThreshold = val

    #设置生成多少页
    def setPageCount(self,val):
        self.__page = val

    #设置生成多少期
    def setScope(self,val):
        self.__scope = val

    #设置函数开始索引
    def setFuncStart(self,val):
        self.__funcStart = val

    #设置函数结束索引
    def setFuncEnd(self,val):
        self.__funcEnd = val

    #初始化数据库，包括生成开奖信息表，概率计算表和初始化概算数据间隔表
    def initData(self,page=33,scope=100):
        self.__page = page
        self.__scope = scope
        #重新生成表的话，就把原来的表全部清空，重头再来一次
        if self.__modb.isOnline:
            self.__modb.clearTermTable()
        else:
            print("离线状态下将使用原有数据进行分析！")
        # 首先生成TermTable中的数据
        self.__modb.createTermTable()
        #不管在线或者离线状态下均可执行数据及概率表的重新生成
        self.__modb.clearLuckyTable()
        self.__modb.clearDataInterval()
        #生成LuckyTable表
        #通过多线程生成
        self.createAllLuckyData(self.__scope,self.__page)

        print("开始生成概率周期数据")
        start = time.time()
        for data in self.__modb.getAllDataInterval():
            self.__modb.updateInterval(data)
        end = time.time()
        print("生成概率周期数据完毕，用时：",end-start)

    def initDataWithZone(self,page=33,scope=100,zone=20):
        self.__page = page
        self.__scope = scope
        self.__zone = zone
        #重新生成表的话，就把原来的表全部清空，重头再来一次
        if self.__modb.isOnline:
            self.__modb.clearTermTable()
        else:
            print("离线状态下将使用原有数据进行分析！")
        # 首先生成TermTable中的数据
        self.__modb.createTermTable()
        #不管在线或者离线状态下均可执行数据及概率表的重新生成
        self.__modb.clearLuckyTable()
        self.__modb.clearDataInterval()
        # 生成LuckyTable表
        # 通过多线程生成
        self.createAllLuckyDataWithZone(self.__scope,self.__page,zone)

        print("开始生成概率周期数据")
        start = time.time()
        for data in self.__modb.getAllDataInterval():
            self.__modb.updateInterval(data)
        end = time.time()
        print("生成概率周期数据完毕，用时：",end-start)

    #此方法为已有最新数据后的生成预测，只有再初始化数据或更新数据后可用
    def createForecastData(self):
        #生成一个termdata
        termData = self.__modb.getTermDatas(0)[0]
        newTerm = term()
        newTerm.termID = str(int(termData['termID']) +1)
        self.termForcast = newTerm.termID
        newTerm.red = []
        newTerm.blue = 0
        #将该数据插入到期数表
        self.__modb.tterm.insert(newTerm.__dict__)
        #生成luckynum
        self.createAllLuckyData(1,self.__page)

    def createAllLuckyData(self,scope,page):
        print("开始生成预测的统计数据表和概率周期表.......")
        start = time.time()
        lock = threading.Lock()

        def run(scope, page):
            lock.acquire()
            try:
                self.__modb.createLuckyTable(scope, page)
            finally:
                lock.release()

        for p in range(page):
            T = threading.Thread(target=run, args=(scope, p+1))
            T.start()
            T.join()
        end = time.time()
        print("生成统计数据及概率周期表完毕，用时：", end - start)

    def createAllLuckyDataWithZone(self,scope,page,zone):
        print("开始生成预测的统计数据表和概率周期表.......")
        start = time.time()
        lock = threading.Lock()

        def run(scope, curpage,zone,redNum):
            lock.acquire()
            try:
                self.__modb.createLuckyTableWithZone(scope, curpage,zone,redNum)
            finally:
                lock.release()
        for p in range(page*zone):
            T = threading.Thread(target=run, args=(scope, p+1,zone,self.__page))
            T.start()
            T.join()
        end = time.time()
        print("生成统计数据及概率周期表完毕，用时：", end - start)

        # 此方法为已有最新数据后的生成预测，只有再初始化数据或更新数据后可用
    def createForecastDataWithZone(self):
        # 生成一个termdata
        termData = self.__modb.getTermDatas(0)[0]
        newTerm = term()
        newTerm.termID = str(int(termData['termID']) + 1)
        self.termForcast = newTerm.termID
        newTerm.red = []
        newTerm.blue = 0
        # 将该数据插入到期数表
        self.__modb.tterm.insert(newTerm.__dict__)
        # 生成luckynum
        # print("\033[3;32m当前的页面设置为%d页,回滚设置为%d\033[1;33m")
        self.createAllLuckyDataWithZone(1, self.__page,self.__zone)

    def getLastOneTermData(self):
        return self.__modb.getTermDatas(0)[0]

    def getLastOneTermID(self):
        return self.getLastOneTermData()['termID']

    def getIntervalData(self,condition):
        return self.__modb.getIntervalDataByCondition(condition)

    def getLuckyNumByDataID(self,dataID):
        condition = {'dataID':dataID}
        print(condition)
        return self.__modb.tlucky.find({'dataID':dataID})[0]

    def getLuckyNumByCondition(self,condition):
        return self.__modb.tlucky.find(condition)

    def saveLuckyNumToFile(self,fileName,termID,numSize):
        datas = []
        with open(fileName, 'w') as f:
            for data in test.getLuckyNumByCondition({'termID': termID}):
                if data['numSize'] == numSize:
                    lm = list(map(str, set(data['num'])))
                    s = "~".join(lm)
                    datas.append(s)
            datas = list(set(datas))
            for d in datas:
                f.write("10/" + d + "/N/0~1~2~3~4/N\r\n")

    def __getLuckyNumInSmallestScope(self,moduleID,groupID,numSize):
        smallestScope = 9999
        condition = {'groupID':groupID,'moduleID':moduleID,'numSize':numSize}
        datas = self.getIntervalData(condition)
        for data in datas:
            if data['last%d5'%numSize] !=-1 and data['last%d5'%numSize] < smallestScope:
                smallestScope = data['last%d5'%numSize]
        return smallestScope

    def isLuckyCanBeUsedBySmallScope(self,termID,moduleID,groupID,numSize):
        smallScope = self.__getLuckyNumInSmallestScope(moduleID,groupID,numSize)
        if smallScope == 9999:
            return True
        #将该组数据排序，以计算最新一期与上一期是否位于最小周期内
        nearData = ""
        temp = []
        datas = self.getIntervalData({'groupID':groupID,'moduleID':moduleID,'numSize':numSize})
        for da in datas:
            temp.append(da)
        for index,data in enumerate(temp):
            if data['termID'] == termID:
                if index >1:
                    nearData = temp[index-1]['termID']
                    break
        print(nearData)
        if countTermSub(termID,nearData) <= smallScope:
            return False
        else:
            return True


if __name__ == '__main__':
    test = calModule()
    test.initDataWithZone()
    test.createForecastDataWithZone()
    test.termForcast = test.getLastOneTermID()
    condition = {'termID': test.termForcast}
    for data in test.getIntervalData(condition):
        moduleID = data['moduleID']
        groupID = data['groupID']
        numSize = data['numSize']
        #从概算周期表中找出moduleID和groupID相同的项
        if test.isLuckyCanBeUsedBySmallScope(test.termForcast,moduleID,groupID,numSize):
            print("\033[3;33m%s期%d页%d组数可以加入文档，继续使用！\033[3;32m"%(test.termForcast,moduleID,groupID))

    test.saveLuckyNumToFile("E:/LuckyNumber/2019143.txt","2019143",5)
