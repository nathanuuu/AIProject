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
        self.makeX()
        self.makeY()


    #### CODE COPIED FROM HW3 SOLUTION ###
    def loss_logistic(self, X, y, theta):
        # output average loss over all examples
        # and gradient of average loss (without regularization term)
        l = np.sum(np.log(1 + np.exp(-y * X.dot(theta))))
        z = 1 / (1 + np.exp(y * X.dot(theta)))
        return l/y.shape[0], -X.T.dot(z * y) / y.shape[0]


    def loss_svm(self, X, y, theta):
        z = y*X.dot(theta)
        l = np.sum(np.maximum(0, 1 - z)) / y.shape[0]
        g = -X.T.dot((z < 1) * y) / y.shape[0]
        return l,g


    def grad_descent(self, lam, loss, T, alpha):
        (X, y) = (self.X, self.Y)
        theta = np.zeros(X.shape[1])
        for _ in xrange(T):
            l,g = loss(X, y, theta)
            theta -= alpha*(g + lam*theta)
        self.theta = theta
        return theta


    def stochastic_grad_descent(self, lam, loss, T, alpha):
        (X, y) = (self.X, self.Y)
        theta = np.zeros(X.shape[1])
        for _ in xrange(T):
            for i in xrange(X.shape[0]):
                l,g = loss(X[i:i+1,:], y[i:i+1], theta)
                theta -= alpha*(g + lam*theta)
        self.theta = theta
        return theta


    def learningAlgo(self):
        print "Alert: ML code copied from HW3 solution"
        self.stochastic_grad_descent(1e-3, self.loss_logistic, 10, 0.001)
        # print self.stochastic_grad_descent(1e-3, self.loss_svm, 10, 0.001)
        # print self.grad_descent(1e-3, self.loss_logistic, 10, 0.001)
        # print self.grad_descent(1e-3, self.loss_svm, 10, 0.001)


    def writeThetaToCSV(self, consolePrint):
        pass


    def testingAlgo(self):
        pass


    def lineOutput(self, x):
        pass
