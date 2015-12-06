# The ML class is the parent class to both the offense learning, and 
# the arrest learning

from TableOp import TableOp
import numpy as np

class ML(object):
    
    def __init__(self, dataArray):
        self.dataArray = dataArray

    def makeDataSets(self):
        learning = 0.7
        training = 0.7
        (self.learningData, self.testingData) = TableOp.randomSplit(
            self.dataArray, learning)
        (self.trainingData, self.validationData) = TableOp.randomSplit(
            self.dataArray, training)
        del self.learningData


    def makeVectors(self):
        self.X = self.makeX()
        self.Y = self.makeY()
        self.theta = self.makeTheta()


    def makeX(self):
        pass


    def makeY(self):
        pass


    def makeTheta(self):
        pass


    def learningAlgo(self):
        pass

    def testingAlgo(self):
        pass

    def lineOutput(self, x):
        pass
