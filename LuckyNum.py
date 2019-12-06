class luckyNum:
    def __init__(self):
        self.termID = '2019001'
        self.moduleID = 0
        self.groupID = 0
        self.last = 999
        self.num = []
        self.numSize = 0
        self.rightNum = -1

class term:
    def __init__(self):
        self.termID = '2019001'
        self.red = []
        self.blue = 0

    def __str__(self):
        return self.termID+"    "+(" ".join(self.red))+"    "+self.blue