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
        print(datas)
        print(len(datas))
        # for index in range(len(datas)+1):
        #     print(datas[index]['termID'],index)
        #     if index == len(datas):
        #         self.termDataUnkonw.termID = str(int(datas[index]['termID'])+1)
        #         self.groupCal(self.__pageID,1,2,self.termDataUnkonw,datas[index])
        #     else:
        #         self.groupCal(self.__pageID,1,2,datas[index],datas[index+1])

    #termdata应该为上期开奖的数据
    #resultdata为本期开奖结果
    def groupCal(self,pageID,funcStart,funcEnd,termdata,resultdata):
        print(termdata['termID'],resultdata['termID'])
        calRes = luckyNum()
        calRes.moduleID = pageID
        groupNum = int(funcEnd / 6)
        calRes.termID = termdata['termID']
        red = list(map(int,termdata['red']))
        blue = int(termdata['blue'])
        termRightData = self.getTermDataRight(resultdata['red'])
        termRightData = list(map(int, termRightData))
        onePageNum = self.calFuncByGroup(funcStart,funcEnd,red,blue)
        for g in range(groupNum):
            calRes.groupID = g+1
            calRes.num = onePageNum[g*6:(g+1)*6]
            calRes.numSize = len(list(set(calRes.num)))
            calRes.rightNum = 0
            for val in termRightData:
                if val in list(set(calRes.num)):
                    calRes.rightNum += 1
            print(calRes.termID,calRes.moduleID,calRes.groupID,calRes.num,calRes.rightNum, calRes.numSize,calRes.last)


    def calFuncByGroup(self,funcStart,funcEnd,red,blue):
        result = []
        for x in range(funcStart,funcEnd+1):
            result.append(eval("jxM%d"%x)(red,blue))
        return result


if __name__ == '__main__':
    start = time.clock()
    calmod = calModule(1)
    calmod.fillTermData(5)
    end = time.clock()
    print("计算时间为：",end-start)