from MyMongo import *
from calfunc import *
from LuckyNum import *

class calModule():
    __modb = myDb()
    def __init__(self):
        self.termData = []



    def fillTermData(self,scope):
        datas = self.__modb.getTermDatas(scope)
        for data in datas:
            self.groupCal(1,6,data)

    def groupCal(self,funcStart,funcEnd,termdata):
        calRes = luckyNum()
        calRes.groupID = funcStart / 7
        calRes.termID = termdata['termID']
        red = list(map(int,termdata['red']))
        blue = int(termdata['blue'])
        calRes.num = self.calFuncByGroup(funcStart,funcEnd,red,blue)
        print(calRes.num)
        calRes.num = list(set(calRes.num))
        print(calRes.num,len(calRes.num))
        calRes.numSize = len(calRes.num)


    def calFuncByGroup(self,funcStart,funcEnd,red,blue):
        result = []
        for x in range(funcStart,funcEnd+1):
            result.append(eval("jxM%d"%x)(red,blue))
        return result


if __name__ == '__main__':
    calmod = calModule()
    calmod.fillTermData(1)