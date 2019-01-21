###################################
# vertex.py
#
# Used by graph.py
#
# Data Structures and Algorithms
# March 20 2018
# Nate Wilson 801034188
###################################

# vertex class represents nodes
from edge import Edge
verbose = False

class Vertex:
    def __init__(self, name):
        self.name = name
        self.adj = {}
        self.abled = True

    # Called by graph.addedge() - connect this vertex to an edge
    def addEdge(self, vertex, weight):
        if self == vertex:
            print('Oops: you cant assign a vertex to itself')
            return
        elif vertex.returnName() in self.adj:
            if verbose: print('This vertex already exists, weight is updated')
            self.adj[vertex.returnName()].updateW(weight)
            return
        self.adj[vertex.returnName()] = Edge(vertex, weight)

    # Called by graph.deleteedge() - delete an edge from this vertex
    def deleteEdge(self, vertex):
        if vertex.returnName() in self.adj.keys():
            self.adj.pop(vertex.returnName())
        else:
            print("Oops: That adjacent vertex doesn't exist")

    # Called by graph.edgedown() - sets edge to disabled
    def edgeDown(self, vertex):
        self.adj[vertex.returnName()].updateAbled(False)

    # Called by graph.edgeup() - sets edge to abled
    def edgeUp(self, vertex):
        self.adj[vertex.returnName()].updateAbled(True)

    # Called by graph.vertexdown() - sets this vertex to disabled
    def downVertex(self):
        self.abled = False

    # Called by graph.vertexup() - sets this vertex to abled
    def upVertex(self):
        self.abled = True

    # Returns the name of this vertex
    def returnName(self):
        return self.name;

    # Return dictionary of edges
    def returnAdj(self):
        return self.adj;

    # returns if abled
    def isAbled(self):
        return self.abled

    # Called by graph.print() - This part prints the Vertex and calls the edge print function for each adjacency
    def toString(self):
        if self.abled:
            str = "{}\n".format(self.name)
        else:
            str = "{} DOWN\n".format(self.name)
        edgeStr = ""
        sort = sorted(self.adj.keys())
        for s in sort:
            edgeStr += " {}\n".format(self.adj[s].toString())
        return (str + edgeStr)
