from MyMongo import *
from calfunc import *
from LuckyNum import *
import time

class calModule():
    __modb = myDb()
    def __init__(self,page):
        self.termData = []
        self.termDataUnkonw = luckyNum()
        self.__pageID = page

    def getTermDataRight(self,data):
        res = []
        for d in data:
            res.append(Right(d))
        return res

    def fillTermData(self,scope):
        datas = self.__modb.getTermDatas(scope)
        for index in range(len(datas)):
            if index > 1:
                self.groupCal(self.__pageID,1,216,datas[index],datas[index-1])


    #termdata应该为本期未开奖的数据
    #resultdata为上期开奖结果
    def groupCal(self,pageID,funcStart,funcEnd,termdata,resultdata):
        groupNum = int(funcEnd / 6)
        red = list(map(int, resultdata['red']))
        blue = int(resultdata['blue'])
        termRightData = self.getTermDataRight(resultdata['red'])

        # 开奖号码位数去重
        termRightData = list(set(map(int, termRightData)))
        # 开奖号码不去重
        # termRightData = list(map(int, termRightData))

        onePageNum = self.calFuncByGroup(funcStart, funcEnd, red, blue)
        for g in range(groupNum):
            calRes = luckyNum()
            calRes.moduleID = pageID
            calRes.termID = termdata['termID']
            calRes.groupID = g+1
            calRes.num = onePageNum[g*6:(g+1)*6]
            calRes.numSize = len(list(set(calRes.num)))
            calRes.rightNum = 0
            for val in termRightData:
                if val in list(set(calRes.num)):
                    calRes.rightNum += 1
            #print(calRes.termID,calRes.moduleID,calRes.groupID,red,termRightData,calRes.num,calRes.rightNum, calRes.numSize,calRes.last)
            self.__modb.tlucky.insert(calRes.__dict__)

    def calFuncByGroup(self,funcStart,funcEnd,red,blue):
        result = []
        for x in range(funcStart,funcEnd+1):
            result.append(eval("jxM%d"%x)(red,blue))
        return result


if __name__ == '__main__':
    start = time.clock()
    calmod = calModule(1)
    calmod.fillTermData(100)
    end = time.clock()
    print("计算时间为：",end-start)