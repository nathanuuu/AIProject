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

    def makeX(self):
        pass


    def makeY(self):
        pass


    def makeTheta(self):
        pass