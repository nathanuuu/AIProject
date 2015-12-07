from ReadData import ReadData as rd
from Offense import Offense
from Arrest import Arrest


class BlotterML(object):

    # Initialize the blotter problem
    def __init__(self, url):
        self.url = url
        self.dataArray = rd.fromURL(self.url)
        # print "Alert: using dummy input"
        # self.dataArray = rd.fromFile("dummyInput.txt")


    # Runs the machine learning problem on offense records
    def runOffense(self, crimeClass, hours, fileName):
        print "Running Offense problem..."
        oML = Offense(self.dataArray, crimeClass, hours)
        oML.makeDataSets()
        oML.makeVectors()
        oML.learningAlgo()
        oML.writeThetaToCSV(False, fileName)


    # Runs the machine learning problem on arrest records
    def runArrest(self, crimeClass, ageClass, fileName):
        print "Running Arrest problem..."
        aML = Arrest(self.dataArray, crimeClass, ageClass)
        aML.makeDataSets()
        aML.makeVectors()
        aML.learningAlgo()
        aML.writeThetaToCSV(False, fileName)


# Create a new instance of the blotter problem from the Police Blotter URL
u = "https://data.wprdc.org/datastore/dump/c0fcc09a-7ddc-4f79-a4c1-9542301ef9dd"
B = BlotterML(u)

# Run Offense ML
# A crime class is passed that indicates what we consider as major offenses
crimeClass = [("DUI", 1.0), ("burglary", 1.0), ("theft", 1.0),
              ("robbery", 1.0), ("arson", 1.0), ("kidnapping", 1.0)]
hours = 1
fn = "offense_data.csv"
B.runOffense(crimeClass, hours, fn)

# Run Arrest ML
# A crime class is passed that indicates whether we want to check if the
# arrested perp is likely to commit any crime with mentioned description
crimeClass = [("possession", 1.0)]
ageClass = [16, 18, 21, 65, 45] # numbers mark the beginning of a class
fn = "arrest_data.csv"
B.runArrest(crimeClass, ageClass, fn)
# we can generate output by calling the lineOutput function of the problem


