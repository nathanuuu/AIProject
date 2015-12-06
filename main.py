from ReadData import ReadData as rd
from Offense import Offense as of


class BlotterML(object):

    # Initialize the blotter problem
    def __init__(self, url):
        self.url = url
        #self.dataArray = rd.fromURL(self.url)
        self.dataArray = rd.fromFile("dummyInput.txt")
        (self.lset, self.vset, self.tset) = 

    # Runs the machine learning problem on arrest records
    def runArrest(self):
        pass

    # Runs the machine learning problem on offense records
    def runOffense(self):
        pass


# Create a new instance of the blotter problem
B = BlotterML("")
# Run it, test it, and generate output