import random

class Stats:


class Athlete:
    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.position = self.getPosition()
        self.posID = self.getPosID()
        
        self.getStats()

    def getStats(self):
        # Stats to generate:
        # Pace: Acceleration / Sprint Speed
        # Shooting: Power / Accuracy / Penalities
        # Passing: Short / Long
        # Dribbling: Agility / Control
        # Defending: Strength / Ball Stealing
        
        #Weights:
        #  Goalie:  | Diving |  Handling   | Kicking |  Speed  | Positioning |
        #  Athlete: |  Pace  |   Shooting  | passing |Dribbling|Defending|
        #          [Acc,speed,power,acc,pen,shrt,long,agil,ctrl,strn,steal]
        # forWeight = [1.0,1.0,1.0,1.0,1.0,0.8,0.75,0.8,0.75,0.4,0.3]
        self.goalieWeight = [0.90,0.90,0.90,0.4,0.90]
        self.forWeight = [0.95,1.00,0.75,0.85,0.40]
        self.midWeight = [0.90,0.85,1.00,0.85,0.60]
        self.defWeight = [0.80,0.40,0.85,0.85,1.00]
         
        if self.
         
        self.stats = {}
        self.stats["Accel"] = random.uniform
    
    def getPosition(self):
        self.posList = ["Forward","Midfielder","Defender","Goaltender"]
        randNum = random.randint(0,100)
        if randNum < 30: return self.posList[0]
        elif randNum < 60: return self.posList[1]
        elif randNum < 90: return self.posList[2]
        else: return self.posList[3]
    
    def getPosID(self):
        return self.posList.index(self.position)
    
    def printInfo(self):
        print("id: %4d | %12s %-12s | pos: %-10s (%d)" % (self.id, self.firstName, self.lastName, self.position, self.posID))
        
    
def getNameList():
    firstNameTxt = "fn.txt"
    lastNameTxt = "ln.txt"
    
    fnFile = open(firstNameTxt)
    lnFile = open(lastNameTxt)
    
    fnList = fnFile.readlines()
    lnList = lnFile.readlines()
    
    fnFile.close()
    lnFile.close()
    
    for n in range(0,len(fnList)):
        fnList[n] = fnList[n].strip()
    
    for n in range(0,len(lnList)):
        lnList[n] = lnList[n].strip()
    
    return fnList, lnList
        
def main():
    fnList, lnList = getNameList()
    numOfAthletes = 1000
    listOfAthletes = []
    
    for n in range(numOfAthletes):
        listOfAthletes.append(Athlete(n, random.choice(fnList), random.choice(lnList)))

    for athlete in listOfAthletes:
        athlete.printInfo()
    
        
if __name__ == "__main__":
    main()