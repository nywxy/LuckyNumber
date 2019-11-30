class luckyNum:
    def __init__(self):
        self.termID = '2019001'
        self.last = 100
        self.rightnum = 0
        self.num = []

class term:
    def __init__(self):
        self.termID = '2019001'
        self.red = []
        self.blue = 0

    def __str__(self):
        return self.termID+"    "+(" ".join(self.red))+"    "+self.blue