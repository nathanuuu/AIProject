# This arrest class is an extension to the ml class

from ML import ML
from TableOp import TableOp
import numpy as np

class Arrest(ML):
    
    def __init__(self, dataArray):
        # we need to take out only arrest data
        self.dataArray = TableOp.takeEntries(dataArray,
            ["REPORT_NAME"], ["ARREST"])
        # and take the stuff we need
        self.dataArray = TableOp.reduceColumns(self.dataArray, 
            ["DESCRIPTION", "ARREST_TIME", "NEIGHBORHOOD", "AGE", "GENDER"])
        # we give each neighborhood a numerical representation
        (self.dataArray, self.nidDict) = TableOp.numerify(
            self.dataArray, "NEIGHBORHOOD")
        self.neighborhoodCount = len(self.nidDict) # number of neighborhoods
        print "Alert: in Arrest, time is 3 hours per interval"
        self.timeIntervals = 60 * 3 # in minutes
        self.timeIntervalCount = 60 * 24 / self.timeIntervals


    def makeX(self):
        pass


    def makeY(self):
        pass