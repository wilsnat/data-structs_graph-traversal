###################################
# minheap.py
#
# Used by graph.py
#
# Data Structures and Algorithms
# March 20 2018
# Nate Wilson 801034188
###################################

import math
from heapobj import Heapobj

#this heap is specifically for heap objects (stores vertex information for Dijsktra's)
class Heap:
    def __init__(self):
        self.a = []
        self.hLen = len(self.a)

    # returns the length of the heap
    def length(self):
        return self.hLen

    # pushes a new heapobject to the heap and reorders it
    def heapPush(self, ho):
        ho.updateI(len(self.a))
        self.a.append(ho)
        self.floatUp(len(self.a))

    # pops the min value object and reorders heap
    def heapPop(self):
        if self.hLen == 1:
            return self.a.pop()
        try:
            popped = self.a[0]
            self.a[0] = self.a.pop()
            self.a[0].updateI(0)
        except IndexError:
            print('ERROR: Heap has size 0')
            return
        self.hLen = len(self.a)
        self.floatDown(0)
        return popped

    # move up from leaves to branches
    def floatUp(self, i):
        p = parent(i)
        while i > 0 and  self.a[i].returnWeight() < self.a[p].returnWeight():
            self.a[p], self.a[i] = self.a[i], self.a[p]
            self.a[i].updateI(i)
            self.a[p].updateI(p)
            i = p
            self.floatUp(i)

    # move down from branches to leaves
    def floatDown(self, i):
        hmin = i
        left = leftIndex(i)
        right = rightIndex(i)
        if right < self.hLen and self.a[right].returnWeight() <= self.a[left].returnWeight():
            if self.a[right].returnWeight() < self.a[hmin].returnWeight():
                self.a[right], self.a[hmin] = self.a[hmin], self.a[right]
                self.a[right].updateI(right)
                self.a[hmin].updateI(hmin)
                self.floatDown(right)
        elif right < self.hLen and self.a[right].returnWeight() > self.a[left].returnWeight():
            self.a[left], self.a[hmin] = self.a[hmin], self.a[left]
            self.a[hmin].updateI(hmin)
            self.a[left].updateI(left)
            self.floatDown(left)

    # sorts an array to represent a heap
    def minHeapify(self, i):
        hmin = i
        left = leftIndex(i)
        if left < self.hLen and self.a[left].returnWeight() < self.a[hmin].returnWeight():
            hmin = left
            self.a[hmin].updateI(hmin)
        right = rightIndex(i)
        if right < self.hLen and self.a[right].returnWeight() < self.a[hmin].returnWeight():
            hmin = right
            self.a[hmin].updateI(hmin)
        if not hmin == i:
            self.a[i], self.a[hmin] = self.a[hmin], self.a[i]
            self.a[hmin].updateI(hmin)
            self.a[i].updateI(i)
            self.minHeapify(hmin)

    # called to initialize the heap
    def buildHeap(self, A):
        self.hLen = len(A)
        self.a = A
        for i in range(0,self.hLen):
            self.a[i].updateI(i)
        i = int(self.hLen / 2 - 1)
        while i >= 0:
            self.minHeapify(i)
            i -= 1

# called by minheap.floatUp - returns the parent index
def parent(i):
    return int((i-1)/2)

# called by minheap.floatDown - returns the left child index
def leftIndex(i):
    return 2 * i + 1

# called by minheap.floatDown - returns the right child index
def rightIndex(i):
    return 2 * i + 2