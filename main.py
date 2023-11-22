import random
import math

class athleteStats:
    def __init__(self,weights,posID):
        self.weightLengths = [2,3,2,2,2] #Number of stats that fall under the category (pace has 2,shooting has 3, etc...)
        self.numOfStats = 0
        for elm in self.weightLengths:
            self.numOfStats += elm
        self.weights = weights
        self.posID = posID
        self.genPlayerStats()
        
    def genPlayerStats(self):
        self.statList = []
        for n in range(self.numOfStats):
            self.statList.append(round(random.gauss(60, 15),1))
            
        n = 0
        self.finalWeights = []
        
        for wgtLenNum in range(len(self.weightLengths)):
            for m in range(n, n+self.weightLengths[wgtLenNum]):
                self.finalWeights.append(self.weights[wgtLenNum])
                n += 1
                
        for m in range(len(self.finalWeights)):
            self.statList[m] = min(round(self.statList[m] * self.finalWeights[m]),99)
            
    def printStats(self):
        print(self.statList)
        

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
        #  Goalie:  | Diving |  Handling   | Kicking |  Speed  |Positioning|
        #  Athlete: |  Pace  |   Shooting  | passing |Dribbling|Defending |
        #          [Acc,speed,power,acc,pen,shrt,long,agil,ctrl,strn,steal]
        self.goalieWeight = [0.90,0.90,0.90,0.6,0.90]
        self.forWeight = [0.95,1.00,0.75,0.85,0.60]
        self.midWeight = [0.90,0.85,1.00,0.85,0.80]
        self.defWeight = [0.80,0.60,0.85,0.85,1.00]
         
        match self.position:
            case "Forward":
                self.stats = athleteStats(self.forWeight,self.posID)
            case "Midfield":
                self.stats = athleteStats(self.midWeight,self.posID)
            case "Defender":
                self.stats = athleteStats(self.defWeight,self.posID)
            case "Goaltender":
                self.stats = athleteStats(self.goalieWeight,self.posID)

    def getPosition(self):
        self.posList = ["Forward","Midfield","Defender","Goaltender"]
        randNum = random.randint(0,100)
        if randNum < 30: return self.posList[0]
        elif randNum < 60: return self.posList[1]
        elif randNum < 90: return self.posList[2]
        else: return self.posList[3]
    
    def getPosID(self):
        return self.posList.index(self.position)
    
    def printInfo(self):
        print("id: %4d | %12s %-12s | pos: %-10s (%d) " % (self.id, self.firstName, self.lastName, self.position, self.posID), end="")
        self.stats.printStats()
        
    
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