from ReadData import ReadData as rd
from Offense import Offense
from Arrest import Arrest


class BlotterML(object):

    # Initialize the blotter problem
    def __init__(self, url):
        self.url = url
        self.dataArray = rd.fromURL(self.url)
        # print "Alert: using dummy input"
        # self.dataArray = rd.fromFile("dummyInput2.txt")

    # Runs the machine learning problem on arrest records
    def runArrest(self):
        aML = Arrest(self.dataArray)
        aML.makeDataSets()
        aML.makeVectors()
        aML.learningAlgo()
        aML.printTheta()

    # Runs the machine learning problem on offense records
    def runOffense(self):
        oML = Offense(self.dataArray)
        oML.makeDataSets()
        oML.makeVectors()
        oML.learningAlgo()


# Create a new instance of the blotter problem
u = "https://data.wprdc.org/datastore/dump/c0fcc09a-7ddc-4f79-a4c1-9542301ef9dd"
B = BlotterML(u)
# Run it
#B.runOffense()
B.runArrest()
# we can generate output by calling the lineOutput function of the problem


