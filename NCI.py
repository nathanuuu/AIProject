# This offense class is an extension to the ml class

from ML import ML
from TableOp import TableOp
from Crime import Crime
import numpy as np

class NCI(ML):

    def __init__(self, dataArray, crimeClass):
        # we store the crimeClass to the problem
        self.crimeClass = crimeClass
        # we need to take out only offense data
        self.dataArray = TableOp.takeEntries(dataArray, 
            ["REPORT_NAME"], ["OFFENSE 2.0"])
        # and take the stuff we need
        self.dataArray = TableOp.reduceColumns(self.dataArray,
            ["DESCRIPTION", "NEIGHBORHOOD"])
        # we give each neighborhood a numerical representation
        (self.dataArray, self.nidDict) = TableOp.numerify(
            self.dataArray, "NEIGHBORHOOD")
        self.neighborhoodCount = len(self.nidDict) # number of neighborhoods


    def makeX(self):
        self.XTable = TableOp.reduceColumns(self.dataArray, 
            ["NEIGHBORHOOD"])
        (self.Xrows, self.Xcols) = (len(self.XTable) - 1, 
            self.neighborhoodCount)
        self.X = [[0.0 for i in xrange(self.Xcols)] for j in xrange(self.Xrows)]
        for i in xrange(len(self.X)):
            self.fillXi(self.X[i], self.XTable[i + 1]) # skip header in table
        self.X = np.array(self.X)


    # Fill the X(i) with data from the ith table entry
    def fillXi(self, xi, ti):
        nbh = ti[0]
        # fill neighborhood
        xi[nbh] = 1.0


    def makeY(self):
        self.YTable = TableOp.reduceColumns(self.dataArray, ["DESCRIPTION"])
        (self.Yrows) = self.Xrows
        self.Y = [0.0 for i in xrange(self.Yrows)]
        for i in xrange(self.Yrows):
            self.Y[i] = Crime.severeness(self.YTable[i + 1][0], 
                self.crimeClass)  # skip header
        self.Y = np.array(self.Y)


    def writeThetaToCSV(self, consolePrint, fileName):
        theta = self.theta.tolist()
        # be safe about theta length
        assert (len(theta) == len(self.nidDict))
        # list to be exported
        exportList = []
        # we export neighborhood data
        for i in xrange(len(self.nidDict)):
            output = [self.nidDict[i], theta[i]]
            exportList.append(output)
            if (consolePrint == True):
                print self.nidDict[i], theta[i]
        # write to files
        od = open(fileName, "w+")
        for i in xrange(len(exportList)):
            od.write(exportList[i][0] + "," + str(exportList[i][1]) + '\n')
        od.close()







