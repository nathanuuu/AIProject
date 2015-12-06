from ReadData import ReadData as rd
from Offense import Offense
from Arrest import Arrest
from TableOp import TableOp as to


class BlotterML(object):

    # Initialize the blotter problem
    def __init__(self, url):
        self.url = url
        #self.dataArray = rd.fromURL(self.url)
        self.dataArray = rd.fromFile("dummyInput.txt")

    # Runs the machine learning problem on arrest records
    def runArrest(self):
        oML = Arrest(self.dataArray)
        oML.makeDataSets()
        oML.makeVectors()

    # Runs the machine learning problem on offense records
    def runOffense(self):
        oML = Offense(self.dataArray)
        oML.makeDataSets()
        oML.makeVectors()


# Create a new instance of the blotter problem
B = BlotterML("")
# Run it, test it, and generate output
B.runOffense()
B.runArrest()