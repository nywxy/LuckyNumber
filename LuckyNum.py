class luckyNum:
    def __init__(self):
        self.dataID = '2001001001001'
        self.termID = '2019001'
        self.moduleID = 0
        self.groupID = 0
        self.num = []
        self.numSize = 0
        self.rightNum = -1

class term:
    def __init__(self):
        self.termID = '2019001'
        self.red = []
        self.blue = 0

    def __str__(self):
        return self.termID+"    "+(" ".join(self.red))+"    "+str(self.blue)

class dataInterval:
    def __init__(self):
        self.dataID = '2001001001001'
        self.termID = '2019001'
        self.moduleID = 0
        self.groupID = 0
        self.numSize = -1
        self.rightNum = -1
        self.last65 = -1
        self.last55 = -1
