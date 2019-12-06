from MyMongo import *
from calfunc import *

class calModule():
    __modb = myDb()
    def __init__(self):
        self.termData = []



    def fillTermData(self,scope):
        datas = self.__modb.getTermDatas(scope)
        for data in datas:
            print(data)



if __name__ == '__main__':
    calmod = calModule()
    calmod.fillTermData(5)