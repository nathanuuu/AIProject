from ReadData import ReadData as rd
from NCI import NCI
from TCI import TCI
from DNI import DNI


class BlotterML(object):

    # Initialize the blotter problem
    def __init__(self, url):
        self.url = url
        # self.dataArray = rd.fromURL(self.url)
        print "Alert: using dummy input"
        self.dataArray = rd.fromFile("dummyInputLarge.txt")


    # Runs the machine learning problem on offense records
    def runTCI(self, crimeClass, hours, fileName):
        print "Running TCI problem..."
        ML = TCI(self.dataArray, crimeClass, hours)
        ML.makeDataSets()
        ML.makeVectors()
        ML.learningAlgo()
        ML.writeThetaToCSV(False, fileName)


    def runNCI(self, crimeClass, fileName):
        print "Running NCI problem..."
        ML = NCI(self.dataArray, crimeClass)
        ML.makeDataSets()
        ML.makeVectors()
        ML.learningAlgo()
        ML.writeThetaToCSV(False, fileName)


    # Runs the machine learning problem on arrest records
    def runDNI(self, crimeClass, ageClass, fileName):
        print "Running DNI problem..."
        aML = DNI(self.dataArray, crimeClass, ageClass)
        aML.makeDataSets()
        aML.makeVectors()
        aML.learningAlgo()
        aML.writeThetaToCSV(False, fileName)


# Create a new instance of the blotter problem from the Police Blotter URL
u = "https://data.wprdc.org/datastore/dump/c0fcc09a-7ddc-4f79-a4c1-9542301ef9dd"
B = BlotterML(u)

ageClass = [16, 21, 35, 45, 65] # numbers mark the beginning of a class

hours = 1

minor_keywords = [("marijuana", 1.0), ("substance", 1.0), ("drunk", 1.0), 
                  ("DUI", 1.0), ("alcohol", 1.0), ("theft", 1.0)]
TCI_minor_fn = "TCI_minor.csv"
NCI_minor_fn = "NCI_minor.csv"
DNI_minor_fn = "DNI_minor.csv"

major_keywords = [("robbery", 1.0), ("arson", 1.0), ("murder", 1.0), 
                  ("assault", 1.0), ("kidnapping", 1.0), ("terror", 1.0), 
                  ("burglar", 1.0), ("conspiracy", 1.0)]
TCI_major_fn = "TCI_major.csv"
NCI_major_fn = "NCI_major.csv"
DNI_major_fn = "DNI_major.csv"

property_keywords = [("burglar", 1.0), ("theft", 1.0), ("robbery", 1.0)]
TCI_property_fn = "TCI_property.csv"
NCI_property_fn = "NCI_property.csv"
DNI_property_fn = "DNI_property.csv"

alcohol_keywords = [("drunk", 1.0), ("DUI", 1.0), ("alcohol", 1.0)]
TCI_alcohol_fn = "TCI_alcohol.csv"
NCI_alcohol_fn = "NCI_alcohol.csv"
DNI_alcohol_fn = "DNI_alcohol.csv"

drug_keywords = [("marijuana", 1.0), ("substance", 1.0)]
TCI_drug_fn = "TCI_drug.csv"
NCI_drug_fn = "NCI_drug.csv"
DNI_drug_fn = "DNI_drug.csv"


####### Run problem on minor crimes
print "Solving for minor crimes"
B.runTCI(minor_keywords, hours, TCI_minor_fn)
B.runNCI(minor_keywords, NCI_minor_fn)
B.runDNI(minor_keywords, ageClass, DNI_minor_fn)
print

####### Run problem on major crimes
print "Solving for major crimes"
B.runTCI(major_keywords, hours, TCI_major_fn)
B.runNCI(major_keywords, NCI_major_fn)
B.runDNI(major_keywords, ageClass, DNI_major_fn)
print

####### Run problem on property crimes
print "Solving for property crimes"
B.runTCI(property_keywords, hours, TCI_property_fn)
B.runNCI(property_keywords, NCI_property_fn)
B.runDNI(property_keywords, ageClass, DNI_property_fn)
print

####### Run problem on alcohol crimes
print "Solving for alcohol crimes"
B.runTCI(alcohol_keywords, hours, TCI_alcohol_fn)
B.runNCI(alcohol_keywords, NCI_alcohol_fn)
B.runDNI(alcohol_keywords, ageClass, DNI_alcohol_fn)
print

####### Run problem on drug crimes
print "Solving for drug crimes"
B.runTCI(drug_keywords, hours, TCI_drug_fn)
B.runNCI(drug_keywords, NCI_drug_fn)
B.runDNI(drug_keywords, ageClass, DNI_drug_fn)
print


