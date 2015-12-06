import urllib

class ReadData(object):

    # A method that turns the file data into a 2D python array
    @staticmethod
    def fromFile(filename):
        f = open(filename, 'r')
        inputString = f.read()
        # fileobj.read() is a string, and we split by '\n' to extract each row
        rowArray = inputString.split('\n')
        return ReadData.makeCellArray(rowArray)


    # A method that turns the online data into a 2D python array
    @staticmethod
    def fromURL(urlname):
        fileobj = urllib.urlopen(urlname)
        inputString = fileobj.read()
        # fileobj.read() is a string, and we split by '\r\n' to extract each row
        rowArray = inputString.split('\r\n')
        return ReadData.makeCellArray(rowArray)


    # A function that takes in a 1D python array of strings, 
    # splits the strings by data separator ','
    # and returns a 2D python array of all data
    @staticmethod
    def makeCellArray(rowArray):
        cellArray = []
        # remove the last row which is empty in rowArray
        for s in rowArray[:-1]:
            line = s.split(',')
            cellArray.append(line)
        return cellArray


##############################
#########   Tests       ######
##############################
print ReadData.fromFile("dummyInput.txt")
# u="https://data.wprdc.org/datastore/dump/c0fcc09a-7ddc-4f79-a4c1-9542301ef9dd"
# print ReadData.fromURL(u)



