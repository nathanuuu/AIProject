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