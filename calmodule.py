from MyMongo import *
from calfunc import *
from LuckyNum import *
import time
import threading

class calModule():
    __modb = myDb()
    def __init__(self):
        self.updateTermData = []
        self.termDataUnkonw = luckyNum()
        self.isUpdate = False
        self.__page = 33   #生成多少页数据
        self.__scope = 100  #生成多少期数据
        self.__intervalThreshold = 10 #查找间隔阈值
        self.__funcStart = 1 #计算函数开始索引
        self.__funcEnd = 216 #计算函数结束索引

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
        print("开始生成统计数据表和概率周期表.......")
        start = time.clock()
        lock = threading.Lock()
        def run(scope,page):
            lock.acquire()
            try:
                self.__modb.createLuckyTable(scope,page)
            finally:
                lock.release()
        for page in range(self.__page+1):
            T = threading.Thread(target=run,args=(self.__scope,page+1))
            T.start()
            T.join()
        end = time.clock()
        print("生成统计数据及概率周期表完毕，用时：",end-start)

        print("开始生成概率周期数据")
        start = time.clock()
        for data in self.__modb.getAllDataInterval():
            self.__modb.updateInterval(data)
        end = time.clock()
        print("生成概率周期数据完毕，用时：",end-start)



if __name__ == '__main__':
    test = calModule()
    test.initData(scope=200)