# This arrest class is an extension to the ml class
# Given the neighborhood, age, gender, predict whether it's type of crime

from ML import ML
from TableOp import TableOp
import numpy as np
from Crime import Crime

class Arrest(ML):
    
    def __init__(self, dataArray):
        # we need to take out only arrest data
        self.dataArray = TableOp.takeEntries(dataArray,
            ["REPORT_NAME"], ["ARREST"])
        # and take the stuff we need
        self.dataArray = TableOp.reduceColumns(self.dataArray, 
            ["DESCRIPTION", "NEIGHBORHOOD", "AGE", "GENDER"])
        # we give each neighborhood a numerical representation
        (self.dataArray, self.nidDict) = TableOp.numerify(
            self.dataArray, "NEIGHBORHOOD")
        self.neighborhoodCount = len(self.nidDict) # number of neighborhoods
        self.ageGroupCount = 6
        self.genderCount = 2
        print len(self.dataArray)


    def makeX(self):
        self.XTable = TableOp.reduceColumns(self.dataArray,
            ["NEIGHBORHOOD", "AGE", "GENDER"])
        self.XTable = TableOp.dropEntries(self.XTable, 
            ["AGE", "GENDER"], ["", ""])
        self.updateAge()
        self.updateGender()
        (self.Xrows, self.Xcols) = (len(self.XTable) - 1, 
            self.neighborhoodCount * self.ageGroupCount * self.genderCount)
        self.X = [[0.0 for i in xrange(self.Xcols)] for j in xrange(self.Xrows)]
        for i in xrange(len(self.X)):
            [n, a, g] = self.XTable[i + 1] # skip header
            index = (n * self.ageGroupCount * self.genderCount
                + a * self.genderCount + g)
            self.X[i][index] = 1.0
        self.X = np.array(self.X)


    def updateAge(self):
        for i in xrange(1, len(self.XTable), 1):
            age = int(self.XTable[i][1])
            if (0 < age < 15):
                self.XTable[i][1] = 0
            elif (15 <= age < 18):
                self.XTable[i][1] = 1
            elif (18 <= age < 21):
                self.XTable[i][1] = 2
            elif (21 <= age < 45):
                self.XTable[i][1] = 3
            elif (45 <= age < 65):
                self.XTable[i][1] = 4
            else:
                self.XTable[i][1] = 5


    def updateGender(self):
        for i in xrange(1, len(self.XTable), 1):
            gender = self.XTable[i][2]
            if (gender == "M"):
                self.XTable[i][2] = 0
            else:
                self.XTable[i][2] = 1


    def makeY(self):
        self.YTable = TableOp.reduceColumns(self.dataArray, ["DESCRIPTION"])
        crimeClass = [("burglary", 1.0)]
        (self.Yrows) = self.Xrows
        self.Y = [0.0 for i in xrange(self.Yrows)]
        print self.YTable
        for i in xrange(len(self.Y)):
            desc = self.YTable[i + 1][0] # skip header
            self.Y[i] = Crime.severeness(desc, crimeClass)
        self.Y = np.array(self.Y)


    def printTheta(self):
        self.printableTheta = self.theta.tolist()
        for i in xrange(len(self.printableTheta)):
            self.printableTheta[i] = (self.recoverLabels(i), 
                self.printableTheta[i])
        self.printableTheta = sorted(self.printableTheta, 
            key = lambda x: x[1], reverse = True)
        for i in xrange(len(self.printableTheta)):
            print self.printableTheta[i]


    def recoverLabels(self, index):
        # gender
        if (index % 2 == 0): 
            sString = "M "
        else: 
            sString = "F "
        # age group
        a = (index % (self.ageGroupCount * self.genderCount)) / self.genderCount
        if (a == 0):
            aString = "under 15 "
        elif (a == 1):
            aString = "15 to 17 "
        elif (a == 2):
            aString = "18 to 20 "
        elif (a == 3):
            aString = "21 to 44 "
        elif (a == 4):
            aString = "45 to 64 "
        else:
            aString = "65 and above "
        # neighborhood
        n = index / (self.genderCount * self.ageGroupCount)
        nString = self.nidDict[n]
        return sString + aString + nString





