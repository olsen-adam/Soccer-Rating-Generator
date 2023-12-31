#!/bin/env python

import random
import math
import time
import csv  
import tqdm


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
            self.statList.append(round(random.gauss(75, 15),1))
            
        n = 0
        self.finalWeights = []
        
        for wgtLenNum in range(len(self.weightLengths)):
            for m in range(n, n+self.weightLengths[wgtLenNum]):
                self.finalWeights.append(self.weights[wgtLenNum])
                n += 1
                
        for m in range(len(self.finalWeights)):
            self.statList[m] = max(round(random.gauss(20,5)),min(round(self.statList[m] * self.finalWeights[m]),99))
            
        self.oldFinalRating = 40
        for m in range(len(self.finalWeights)):
            self.oldFinalRating += self.statList[m]
            
    def printStats(self):
        print("Raw Rating: %d Final Rating: %d" % (self.oldFinalRating,self.newFinalRating),self.statList)
        
    def getOldRating(self):
        return self.oldFinalRating
        
    def adjustFinal(self,min,max,minRating,maxRating):
        # { [ (final - min) / (max - min) ] * (maxRating - minRating) } + minRating
        #           a               b                    c                     
        a = self.oldFinalRating - min
        b = max - min
        c = maxRating - minRating
        self.newFinalRating = (((a/b)*c)+minRating)
        
    def getStats(self):
        return self.statList

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
        self.goalieWeight = [0.90,0.90,0.90,0.8,0.90]
        self.forWeight = [0.95,1.00,0.90,0.90,0.80]
        self.midWeight = [0.90,0.95,1.00,0.90,0.85]
        self.defWeight = [0.85,0.85,0.90,0.85,1.00]
         
        match self.position:
            case "Forward":
                self.stats = athleteStats(self.forWeight,self.posID)
            case "Midfield":
                self.stats = athleteStats(self.midWeight,self.posID)
            case "Defender":
                self.stats = athleteStats(self.defWeight,self.posID)
            case "Goaltender":
                self.stats = athleteStats(self.goalieWeight,self.posID)

    def adjustStats(self,min,max,minRating,maxRating):
        self.stats.adjustFinal(min,max,minRating,maxRating)

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
        
    def returnStats(self):
        # ["FirstName","LastName","Position","FinalRating","Acc","Speed","Power","Accuracy",
        # "Penalty","ShortPass","LongPass","Agility","Control","Strength","Stealing"]
        currLine = [self.firstName,self.lastName,self.getPosition(),round(self.stats.newFinalRating,3)]
        for stats in self.stats.getStats():
            currLine.append(stats)
            
        return currLine
        
        
    
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

def writeToFile(listOfAthletes,nameUnit,barFormat,nameOfFile):
    writeMode = 'w'
    newLineChar = ''
    with open(nameOfFile,writeMode,newline=newLineChar) as csvFile:
        fileWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fileWriter.writerow(["FirstName","LastName","Position","FinalRating","Acc","Speed","Power","Accuracy","Penalty","ShortPass","LongPass","Agility","Control","Strength","Stealing"])
        for athlete in tqdm.tqdm(listOfAthletes, desc="%40s" % "Adding Athletes to CSV File", unit=nameUnit, bar_format=barFormat):
            fileWriter.writerow(athlete.returnStats())
        
def main():
    startTime = time.time()
    fnList, lnList = getNameList()
    nameOfCSVFile = "playerList.csv"
    numOfAthletes = 20000
    listOfAthletes = []
    nameUnit = " Athletes"
    numBars = 20
    barFormat = '{l_bar}{bar:%d}{r_bar}{bar:-%db}' % (numBars,numBars)
    
    for n in tqdm.trange(numOfAthletes, desc="%40s" % "Generating Athletes with Random Names", unit=nameUnit, bar_format=barFormat):
        listOfAthletes.append(Athlete(n, random.choice(fnList), random.choice(lnList)))

    finalStats = []
    for athlete in tqdm.tqdm(listOfAthletes,desc="%40s" % "Adjusting Athletes Overall Rating", unit=nameUnit, bar_format=barFormat):
        finalStats.append(athlete.stats.getOldRating())

    minRating = 45
    maxRating = 93
    for n in tqdm.trange(numOfAthletes, desc="%40s" % "Adjusting Athletes Final Stats", unit=nameUnit, bar_format=barFormat):
        athlete = listOfAthletes[n]
        athlete.adjustStats(min(finalStats),max(finalStats),minRating,maxRating)
    
    try:
        writeToFile(listOfAthletes,nameUnit,barFormat,nameOfCSVFile)
    except Exception as E:
        print("Error while creating CSV File (%s)" % E)
    finally:
        print("\nSuccesfully Created CSV File (%s) in %.3f Seconds!" % (nameOfCSVFile,time.time() - startTime))
    
        
if __name__ == "__main__":
    main()