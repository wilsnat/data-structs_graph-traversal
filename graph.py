###################################
# graph.py
#
# A network representation that can be
# edited and analyized for the shortest path
#
# run >>python graph.py networkFile.txt
# to build network
#
# Data Structures and Algorithms
# March 20 2018
# Nate Wilson 801034188
###################################

from vertex import Vertex
from minheap import Heap
from heapobj import Heapobj
import sys


# graph represents the entire network
class Graph():
    # Builds initial tree with undirected edges. Then moves to listen for calls until quit.
    def __init__(self, initList):
        self.vd = {}  # vertex dictionary
        for line in initList:
            if line[0] not in self.vd:
                self.vd[line[0]] = Vertex(line[0])
            if line[1] not in self.vd:
                self.vd[line[1]] = Vertex(line[1])
        for line in initList:
            self.vd[line[0]].addEdge(self.vd[line[1]], float(line[2]))
            self.vd[line[1]].addEdge(self.vd[line[0]], float(line[2]))
        self.sort = sorted(self.vd.keys())
        self.sortAdj = {}  # for reachable
        for vert in self.sort:
            self.sortAdj[vert] = False

    def sortVerts(self):
        self.sort = sorted(self.vd.keys())
        self.sortAdj = {}  # for reachable
        for vert in self.sort:
            self.sortAdj[vert] = False

    # addedge tailvertex headvertex trasmittime
    # adds edge from tailvertex to headvertex
    def addedge(self, tailvertex, headvertex, trasmittime):
        if not tailvertex in self.vd.keys():
            self.vd[tailvertex] = Vertex(tailvertex)
            self.sortVerts()
        if not headvertex in self.vd.keys():
            self.vd[headvertex] = Vertex(headvertex)
            self.sortVerts()
        self.vd[tailvertex].addEdge(self.vd[headvertex], trasmittime)

    # deleteedge tailvertex headvertex
    # deletes edge from tailvertex to headvertex
    def deleteedge(self, tailvertex, headvertex):
        self.vd[tailvertex].deleteEdge(self.vd[headvertex])

    # edgedown tailvertex headvertex
    # sets edge as down from tailvertex to headvertex
    def edgedown(self, tailvertex, headvertex):
        self.vd[tailvertex].edgeDown(self.vd[headvertex])

    # edgeup tailvertex headvertex
    # sets edge as up from tailvertex to headvertex
    def edgeup(self, tailvertex, headvertex):
        self.vd[tailvertex].edgeUp(self.vd[headvertex])

    # vertexdown vertex
    # sets vertex as down
    def vertexdown(self, vertex):
        self.vd[vertex].downVertex()

    # vertexup vertex
    # sets vertex as up
    def vertexup(self, vertex):
        self.vd[vertex].upVertex()

    # path from_vertex to_vertex
    # prints shortest path from_vertex to_vertex and total traversal weight
    def path(self, from_vertex, to_vertex):
        if not (self.vd[from_vertex].isAbled() and self.vd[to_vertex].isAbled()):
            print("One of the nodes is disabled, no path exists")
            return
        e, p = {}, {}
        q = []
        for k in self.vd.keys():
            if self.vd[k].isAbled():
                if not k == from_vertex:
                    e[k] = Heapobj(k, float(sys.maxsize))
                else:
                    e[k] = Heapobj(k, 0)
                p[k] = ""
                q.append(e[k])
        minDist = Heap()
        minDist.buildHeap(q)

        while minDist.length() != 0:
            shortEdge = minDist.heapPop()
            if shortEdge.returnName() == to_vertex:
                if shortEdge.returnWeight() >= sys.maxsize:
                    print("No path exists")
                    return
                else:
                    node = shortEdge.returnName()
                    pStr = node
                    while p[node] != "":
                        node = p[node]
                        pStr = "{} ".format(node) + pStr
                    pStr += " {}".format(round(shortEdge.returnWeight(), 2))
                    print(pStr)
                    return
            for a in self.vd[shortEdge.returnName()].returnAdj():
                if self.vd[a].isAbled() and self.vd[shortEdge.returnName()].returnAdj()[a].isAbled():
                    edgeSum = self.vd[shortEdge.returnName()].returnAdj()[a].returnWeight() + shortEdge.returnWeight()
                    if edgeSum < e[a].returnWeight():
                        e[a].updateW(edgeSum)
                        p[a] = shortEdge.returnName()
                        minDist.floatUp(e[a].returnIndex())

    # print
    # prints adjacent vertices and weights
    def graphToString(self):
        str = ""
        for s in self.sort:
            str += self.vd[s].toString()
        str = str[0:len(str) - 1]  # one too many returns
        print(str)

    # reachable
    # lists all nodes reachable by each node
    # Should be O(V*(|V|+|E|), every object is running a DFS so it is the length of a DFS (O(|V|+|E|) * every node V
    # Note: I took special care not to allow the sorting of the nodes into alphabetical order to affect the
    # run time. The sorting is done when the graph is set up and is simply marked down as visited or not, then it is
    # printed in order by iterating through each node. This takes O(V*(V+V+E)) time instead of O(V*(V+E*logE)) where
    # logE is the assumed sort time of the built in sort function.
    def reachable(self):
        for vert in self.sort:
            if self.vd[vert].isAbled():
                print(vert)
                self.dfs(vert, [vert])
            for s in self.sortAdj.keys():
                if self.sortAdj[s]:
                    print(" {}".format(s))
                self.sortAdj[s] = False

    def dfs(self, vert, visited):
        edges = self.vd[vert].returnAdj()
        for edge in edges:
            if self.vd[edge].isAbled() and edges[edge].isAbled() and edge not in visited:
                visited.append(edge)
                self.sortAdj[edge] = True
                self.dfs(edge, visited)

    # isVert vertex
    # return True if vert is in graph
    def isVert(self, vertex):
        if vertex in self.vd:
            return True
        else:
            return False


# interpreter
# watches for calls
def interpreter(cmd):
    cmdA = cmd.split(' ')
    if cmdA[0] == 'addedge':
        if quickCheck(cmdA, 3):
            network.addedge(cmdA[1], cmdA[2], float(cmdA[3]))
    elif cmdA[0] == 'deleteedge':
        if quickCheck(cmdA, 2):
            network.deleteedge(cmdA[1], cmdA[2])
    elif cmdA[0] == 'edgedown':
        if quickCheck(cmdA, 2):
            network.edgedown(cmdA[1], cmdA[2])
    elif cmdA[0] == 'edgeup':
        if quickCheck(cmdA, 2):
            network.edgeup(cmdA[1], cmdA[2])
    elif cmdA[0] == 'vertexdown':
        if quickCheck(cmdA, 1):
            network.vertexdown(cmdA[1])
    elif cmdA[0] == 'vertexup':
        if quickCheck(cmdA, 1):
            network.vertexup(cmdA[1])
    elif cmdA[0] == 'path':
        if quickCheck(cmdA, 2):
            network.path(cmdA[1], cmdA[2])
    elif cmdA[0] == 'print':
        network.graphToString()
    elif cmdA[0] == 'reachable':
        network.reachable()
    elif cmdA[0] == 'help':
        print('addedge tailvertex headvertex trasmittime\ndeleteedge tailvertex headvertex\nedgedown tailvertex '
              'headvertex\nedgeup tailvertex headvertex\nvertexdown vertex\nvertexup vertex\npath from_vertex '
              'to_vertex\nprint\nreachable')
    elif cmdA[0] == 'quit':
        quit()
    else:
        print('Please use valid command')

#checks if it has the right number of args
def quickCheck(cmd, argn):
    if len(cmd) - 1 == argn:
        if argn == 3:
            return wCheck(cmd[3])
        elif argn == 2:
            return vertCheck(cmd[1]) and vertCheck(cmd[2])
        else:
            return vertCheck(cmd[1])
    else:
        print("Please use {} argument(s)".format(argn))
        return False

#checks if vert is valid
def vertCheck(vert):
    if network.isVert(vert):
        return True
    else:
        print('Please use valid vertex')
        return False

#checks if weight is a valid float
def wCheck(weight):
    try:
        if float(weight) >= 0:
            return True
        else:
            print('Please use positive weight')
            return False
    except TypeError and ValueError:
        print('Please use valid weight')
        return False


# read from file
def networkRead(filename):
    try:
        results = []
        with open(filename, 'r', encoding='utf-8') as inputfile:
            for line in inputfile:
                results.append(line.strip().split(' '))
        return results
    except FileNotFoundError or UnicodeDecodeError:
        print("File not found. Please use valid file")
        quit()


# main class called on a run.
def main():
    while looper:
        try:
            cmd = input()
            interpreter(cmd)
        except EOFError:
            quit()


looper = True
filename = sys.argv[1]
network = Graph(networkRead(filename))
main()
