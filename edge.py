###################################
# edge.py
#
# Used by graph.py
#
# Data Structures and Algorithms
# March 20 2018
# Nate Wilson 801034188
###################################

#edge class represents connections between nodes
class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.abled = True

    # updates the weight of the edge
    def updateW(self, weight):
        self.weight = weight

    # sets the abled variable to disabled or abled
    def updateAbled(self, bool):
        self.abled = bool

    # returns the weight of the edge
    def returnWeight(self):
        return self.weight

    # returns the name of the vertex it points to
    def returnName(self):
        return self.vertex.returnName()

    # returns if abled
    def isAbled(self):
        return self.abled

    # called by vertex.toString - Returns the vertex it points to and it's weight
    def toString(self):
        if self.abled:
            return "{} {}".format(self.returnName(),self.weight)
        else:
            return "{} {} DOWN".format(self.returnName(), self.weight)
