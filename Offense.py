# This offense class is an extension to the ml class

from ML import ML
from TableOp import TableOp
from Crime import Crime
import numpy as np

class Offense(ML):

    def __init__(self, dataArray, crimeClass, hours):
        try:
            assert(type(hours) == int and 24 % hours == 0)
        except AssertionError:
            hours = 1
        self.hours = hours
        # we store the crimeClass to the problem
        self.crimeClass = crimeClass
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
        self.timeIntervals = 60 * hours # in minutes
        self.timeIntervalCount = 60 * 24 / self.timeIntervals


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
            self.Y[i] = Crime.severeness(self.YTable[i + 1][0], 
                self.crimeClass)  # skip header
        self.Y = np.array(self.Y)


    def writeThetaToCSV(self, consolePrint):
        theta = self.theta.tolist()
        # be safe about theta length
        assert (len(theta) == len(self.nidDict) + self.timeIntervalCount)
        # list to be exported
        exportList = []
        # we first export neighborhood data, then time data
        for i in xrange(len(self.nidDict)):
            output = [self.nidDict[i], theta[i]]
            exportList.append(output)
            if (consolePrint == True):
                print self.nidDict[i], theta[i]
        for i in xrange(self.timeIntervalCount):
            output = [self.timeString(i), theta[i]]
            exportList.append(output)
            if (consolePrint == True):
                print output[0], output[1]
        # write to files
        od = open("offense_data.csv", "w+")
        for i in xrange(len(exportList)):
            od.write(exportList[i][0] + "," + str(exportList[i][1]) + '\n')
        od.close()


    def timeString(self, i):
        startHour = i * self.hours % 24
        endHour = (i + 1) * self.hours % 24
        return "%d:00 ~ %d:00" % (startHour, endHour)







