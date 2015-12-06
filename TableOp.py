# This class contains all the methods on manipulating data. 
# Original data are read only. All methods return new tables.

import copy
import random
import numpy as np

class TableOp(object):
    
    # A method that processes the 2D array matrix table and returns
    # a new 2D array matrix table where the entries in the first input list
    # is equal to the entries in the second input list respectively
    # Exact match required, case sensitive
    @staticmethod
    def takeEntries(table, labels, values):
        assert(len(labels)  == len(values))
        headers = table[0] # the headers of all the data
        indices = copy.deepcopy(labels)
        # We find all the indices of the labels provided, 
        # if no such index can be found, a None is placed
        for i in xrange(len(indices)):
            try:
                indices[i] = headers.index(indices[i])
            except ValueError:
                indices[i] = None
        # Then we create a new table where only the entries that meet
        # the criteria would be preserved
        newTable = []
        newTable.append(copy.deepcopy(table[0]))
        for j in xrange(1, len(table), 1):
            eligibility = True
            for k in xrange(len(indices)):
                # invalid entry header name
                if (indices[k] == None):
                    continue
                # the entry does not match the value
                if (table[j][indices[k]] != values[k]):
                    eligibility = False
                    break   # no more checking necessary
            # copy into newTable if it meets the criteria
            if (eligibility == True):
                newTable.append(copy.deepcopy(table[j]))
        return newTable


    # A method that processes the 2D array matrix table, 
    # and reduces the table to only the columns with labels 
    # mentioned in the argument list
    @staticmethod
    def reduceColumns(table, labels):
        headers = table[0] # the headers of all the data
        indices = copy.deepcopy(labels)
        # We find all the indices of the labels provided, 
        # if no such index can be found, a None is placed
        for i in xrange(len(indices)):
            try:
                indices[i] = headers.index(indices[i])
            except ValueError:
                indices[i] = None
        # Then we create a new table where only the entries that meet
        # the criteria would be preserved
        newTable = []
        for j in xrange(len(table)):
            newEntry = []
            for k in xrange(len(indices)):
                if (indices[k] == None):
                    continue
                newEntry.append(table[j][indices[k]])
            newTable.append(newEntry)
        return newTable


    # A method that randomly selects a portion of the table input based
    # on the portion input in a decimal number
    @staticmethod
    def randomSplit(table, p):
        pTable = []
        qTable = []
        # keep the headers
        pTable.append(table[0])
        qTable.append(table[0])
        for i in xrange(1, len(table), 1):
            if (random.random() < p):
                pTable.append(copy.deepcopy(table[i]))
            else:
                qTable.append(copy.deepcopy(table[i]))
        return (pTable, qTable)

##############################
#########   Tests       ######
##############################

# from ReadData import ReadData as rd

# table = rd.fromFile("dummyInput.txt")
# # All male arrests
# print TableOp.takeEntries(table, ["REPORT_NAME", "GENDER"], ["ARREST", "M"])
# # Reduce report to only these columns
# print TableOp.reduceColumns(table, 
#     ["REPORT_NAME","DESCRIPTION","ARREST_TIME","NEIGHBORHOOD","AGE","GENDER"])
# # random split the data
# (pt, qt) = TableOp.randomSplit(table, 0.7)
# print (len(pt), len(qt))