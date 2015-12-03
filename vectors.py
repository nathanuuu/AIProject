import urllib

# # Download the data from URL
# url = "https://data.wprdc.org/datastore/dump/c0fcc09a-7ddc-4f79-a4c1-9542301ef9dd"
# fileobj = urllib.urlopen(url)
# inputString = fileobj.read()
# # fileobj.read() is a string, and we split by '\r\n' to extract each row
# dataArray = inputString.split('\r\n')

# Use dummyInput.txt
f = open('dummyInput.txt', 'r')
inputString = f.read()
# fileobj.read() is a string, and we split by '\n' to extract each row
dataArray = inputString.split('\n')
"""
# then we create a dictionary for offense or arrest
dataDict = dict()
arrestDict = dict()
offenseDict = dict()

for entry in dataArray[1:-1]:
    values = entry.split(',')
    index = int(values[0])
    dataDict[index] = values
    if (values[1] == 'ARREST'):
        arrestDict[index] = values
    elif (values[1] == 'OFFENSE 2.0'):
        offenseDict[index] = values
"""

class ReadData(object):
    @staticmethod
    def fromFile(filename):
        f = open('dummyInput.txt', 'r')
        inputString = f.read()
        # fileobj.read() is a string, and we split by '\n' to extract each row
        dataArray = inputString.split('\n')

    @staticmethod
    def fromURL(urlname):
        fileobj = urllib.urlopen(url)
        inputString = fileobj.read()
        # fileobj.read() is a string, and we split by '\r\n' to extract each row
        dataArray = inputString.split('\r\n')

arrest_description = []
arrest_time = []
arrest_neighborhood = []
arrest_zone = []
arrest_age = []
arrest_gender = []
offense_description = []
offense_time = []
offense_neighborhood = []
offense_zone = []

for entry in dataArray[1:-1]:
    values = entry.split(',')
    index = int(values[0])
    if (values[1] == 'ARREST'):
        arrest_description.append(values[4])
        arrest_time.append(int(values[5][11]+values[5][12])/6)
        #arrest_neighborhood.append(values[7])
        arrest_zone.append(int(values[8]))
        arrest_age.append(int(values[9]))
        arrest_gender.append(values[10])
    elif (values[1] == 'OFFENSE 2.0'):
        offense_description.append(values[4])
        offense_time.append(int(values[5][11]+values[5][12])/6)
        #offense_neighborhood.append(values[7])
        offense_zone.append(int(values[8]))

offense_time_zone = []
for i in range(len(offense_time)):
    feature = []
    for j in range(10):
        feature.append(0)
    offense_time_zone.append(feature)

for i in range(len(offense_time)):
    offense_time_zone[i][offense_time[i]] = 1
    if (offense_zone[i] != 1): offense_time_zone[i][2+offense_zone[i]] = 0.5
    elif (offense_zone[i] == 1): offense_time_zone[i][9] = 0.5
    offense_time_zone[i][3+offense_zone[i]] = 1
    if (offense_zone[i] != 6): offense_time_zone[i][4+offense_zone[i]] = 0.5
    elif (offense_zone[i] == 6): offense_time_zone[i][4] = 0.5

