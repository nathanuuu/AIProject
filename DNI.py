# This arrest class is an extension to the ml class
# Given the neighborhood, age, gender, predict whether it's type of crime

from ML import ML
from TableOp import TableOp
import numpy as np
from Crime import Crime

class DNI(ML):
    
    def __init__(self, dataArray, crimeClass, ageClass):
        self.crimeClass = crimeClass
        self.ageClass = sorted(ageClass)
        if (len(self.ageClass) == 0):
            self.ageClass = [16, 18, 21, 45, 65]
        # we need to take out only arrest data
        self.dataArray = TableOp.takeEntries(dataArray,
            ["REPORT_NAME"], ["ARREST"])
        # we drop entries where data are not complete
        self.dataArray = TableOp.dropEntries(self.dataArray, 
            ["AGE", "GENDER"], ["", ""])
        # and take the stuff we need
        self.dataArray = TableOp.reduceColumns(self.dataArray, 
            ["DESCRIPTION", "NEIGHBORHOOD", "AGE", "GENDER"])
        # we give each neighborhood a numerical representation
        (self.dataArray, self.nidDict) = TableOp.numerify(
            self.dataArray, "NEIGHBORHOOD")
        self.neighborhoodCount = len(self.nidDict) # number of neighborhoods
        self.ageGroupCount = len(self.ageClass) + 1
        self.genderCount = 2


    def makeX(self):
        self.XTable = TableOp.reduceColumns(self.dataArray,
            ["NEIGHBORHOOD", "AGE", "GENDER"])
        self.updateAge()
        self.updateGender()
        # size is the cross product of all feature sizes
        (self.Xrows, self.Xcols) = (len(self.XTable) - 1, 
            self.neighborhoodCount * self.ageGroupCount * self.genderCount)
        self.X = [[0.0 for i in xrange(self.Xcols)] for j in xrange(self.Xrows)]
        # figure out what each the values are
        for i in xrange(len(self.X)):
            [n, a, g] = self.XTable[i + 1] # skip header
            index = (n * self.ageGroupCount * self.genderCount
                    + a * self.genderCount + g)
            self.X[i][index] = 1.0
        # convert numpy array
        self.X = np.array(self.X)


    def updateAge(self):
        for i in xrange(1, len(self.XTable), 1):
            # invalid data are thrown out
            age = int(self.XTable[i][1])
            if (age >= self.ageClass[self.ageGroupCount - 1 - 1]):
                self.XTable[i][1] = self.ageGroupCount - 1
            else:
                for j in xrange(self.ageGroupCount - 1):
                    if (self.ageClass[j] > age):
                        self.XTable[i][1] = j
                        break


    def updateGender(self):
        for i in xrange(1, len(self.XTable), 1):
            gender = self.XTable[i][2]
            if (gender == "M"):
                self.XTable[i][2] = 0
            else:
                self.XTable[i][2] = 1


    def makeY(self):
        self.YTable = TableOp.reduceColumns(self.dataArray, ["DESCRIPTION"])
        crimeClass = self.crimeClass
        (self.Yrows) = self.Xrows
        self.Y = [0.0 for i in xrange(self.Yrows)]
        for i in xrange(len(self.Y)):
            desc = self.YTable[i + 1][0] # skip header
            self.Y[i] = Crime.severeness(desc, crimeClass)
        self.Y = np.array(self.Y)


    def recoverLabels(self, index):
        # gender
        if (index % 2 == 0): 
            sString = "M"
        else: 
            sString = "F"
        # age group
        a = (index % (self.ageGroupCount * self.genderCount)) / self.genderCount
        if (a == 0):
            aString = "under %d" % self.ageClass[0]
        elif (a == self.ageGroupCount - 1):
            aString = "%d and over" % self.ageClass[-1]
        else:
            aString = "%d to %d" % (self.ageClass[a-1], self.ageClass[a] - 1)
        # neighborhood
        n = index / (self.genderCount * self.ageGroupCount)
        nString = self.nidDict[n]
        return [sString, aString, nString]


    def writeThetaToCSV(self, consolePrint, fileName):
        theta = self.theta.tolist()
        exportList = []
        for i in xrange(len(theta)):
            output = self.recoverLabels(i)
            output.append(str(theta[i]))
            if (consolePrint == True):
                print output[0], output[1], output[2], output[3]
            exportList.append(output)
        # write to file
        ad = open(fileName, "w+")
        for i in xrange(len(exportList)):
            ad.write(exportList[i][0] + "," + str(exportList[i][1]) + ',' +
                exportList[i][2] + "," + str(exportList[i][3]) + '\n')
        ad.close()


