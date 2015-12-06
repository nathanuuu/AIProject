# The ML class is the parent class to both the offense learning, and 
# the arrest learning

from TableOp import TableOp
import numpy as np

class ML(object):
    
    def __init__(self, dataArray):
        self.dataArray = dataArray

    def makeDataSets(self):
        print "Alert: all data sets are used for training"
        learning = 1.0
        training = 1.0
        (learningData, self.testingData) = TableOp.randomSplit(
            self.dataArray, learning)
        (self.trainingData, self.validationData) = TableOp.randomSplit(
            learningData, training)


    def makeVectors(self):
        self.X = self.makeX()
        self.Y = self.makeY()
        self.theta = self.makeTheta()


    # def makeX(self):
    #     pass


    # def makeY(self):
    #     pass


    # def makeTheta(self):
    #     pass


    def learningAlgo(self):
        pass


    def testingAlgo(self):
        pass


    def lineOutput(self, x):
        pass
