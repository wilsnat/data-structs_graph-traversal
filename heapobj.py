###################################
# heapobj.py
#
# Used by graph.py
#
# Data Structures and Algorithms
# March 20 2018
# Nate Wilson 801034188
###################################

#buffer object to allow pointers to work properly in Python
class Heapobj:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.index = 0

    # updates the weight of a path
    def updateW(self, weight):
        self.weight = weight

    # updates the index location in the heap (this is used to float up with out searching the heap)
    def updateI(self, index):
        self.index = index

    # returns the current index
    def returnIndex(self):
        return self.index

    # returns the total weight of a path
    def returnWeight(self):
        return self.weight

    # returns the vertex name that the heap obj points to
    def returnName(self):
        return self.name
