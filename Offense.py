# This offense class is an extension to the ml class

from ML import ML
from TableOp import TableOp
from Crime import Crime
import numpy as np

class Offense(ML):

    def __init__(self, dataArray):
        # we need to take out only offense data
        self.dataArray = TableOp.takeEntries(dataArray, 
            ["REPORT_NAME"], ["OFFENSE 2.0"])
        # and take the stuff we need
        self.dataArray = TableOp.reduceColumns(self.dataArray,
            ["DESCRIPTION", "ARREST_TIME", "NEIGHBORHOOD"])
        # we give each neighborhood a numerical representation
        (self.dataArray, self.nidDict) = TableOp.numerify(
            self.dataArray, "NEIGHBORHOOD")
        self.neighborhoodCount = len(self.nidDict) # number of neighborhoods
        print "Alert: in Offense, time is 1 hours per interval"
        self.timeIntervals = 60 * 1 # in minutes (60 minutes * some hours)
        self.timeIntervalCount = 60 * 24 / self.timeIntervals
        print self.nidDict


    def makeX(self):
        print "Alert: in Offense, time interval is 1 or 0"
        self.XTable = TableOp.reduceColumns(self.dataArray, 
            ["ARREST_TIME", "NEIGHBORHOOD"])
        (self.Xrows, self.Xcols) = (len(self.XTable) - 1, 
            self.neighborhoodCount + self.timeIntervalCount)
        self.X = [[0.0 for i in xrange(self.Xcols)] for j in xrange(self.Xrows)]
        for i in xrange(len(self.X)):
            self.fillXi(self.X[i], self.XTable[i + 1]) # skip header in table
        self.X = np.array(self.X)


    #### NEEDS CHANGE ######
    # Fill the X(i) with data from the ith table entry
    def fillXi(self, xi, ti):
        (time, nbh) = (ti[0], ti[1])
        # fill neighborhood
        xi[nbh] = 1.0
        #fill time
        [date, hms] = time.split("T")
        minute = int(hms[0:2]) * 60 + int(hms[3:5])
        intervalIdx = minute / self.timeIntervals
        xi[intervalIdx + self.neighborhoodCount] = 1.0


    def makeY(self):
        self.YTable = TableOp.reduceColumns(self.dataArray, ["DESCRIPTION"])
        (self.Yrows) = self.Xrows
        self.Y = [0.0 for i in xrange(self.Yrows)]
        for i in xrange(self.Yrows):
            self.Y[i] = self.fillYi(self.YTable[i + 1][0])  # skip header
        self.Y = np.array(self.Y)


    #### NEEDS CHANGE ######
    def fillYi(self, desc):
        return Crime.severeness(desc)

