class bodyregion:
    def __init__(self, name, severity):
        self.name = name
        self.severity = severity
    def getscore(self):
        if self.severity == "No Injury":
            return 0
        elif self.severity == "Minor":
            return 1
        elif self.severity == "Moderate":
            return 2
        elif self.severity == "Serious":
            return 3
        elif self.severity == "Severe":
            return 4
        elif self.severity == "Critical":
            return 5
        else:
            return 6

class body:
    def __init__(self, regions):
        self.regions = regions

    def calculatescore(self):
        biggest = []
        loops = 0
        totalscore = 0
        while loops < 3:
            number = 0
            for i in range(len(self.regions)):
                if self.regions[i].getscore() > number:
                    number = i
            biggest.append(self.regions[number])
            self.regions.pop(number)
            if loops < 3:
                loops += 1
                continue
            else:
                break
        for i in range(len(biggest)):
            score = biggest[i].getscore()
            if score == 6:
                totalscore = 75
            else:
                totalscore += (score * score)
        return totalscore     