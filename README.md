# graph.py

###################################

A network representation that can be
edited and analyized for the shortest path

run >>python graph.py networkFile.txt
to build network

###################################

NOTE: Prints any errors, if you find any, are caught and print a warning

Design: There is a graph, vertex, edge structure for the network. The heapobj and minheap are used exclusively for the shortest path algorithm.

Main complex functions:

path(): prints shortest path from_vertex to_vertex and total traversal weight

	Should be O(V(logV)+E). It runs Dijskra's algorithm.
	To avoid incuring a V time penalty for searching through the minheap
	to update a weight, instead I used a dictionary that pointed at the heapobj which allowed instant
	access to update the weight. The heapobj also contains the index that it holds in the minheap and
	is updated anytime the heap is changed. This allows for float up calls to happen on the index we
	updated the weight (O(logV)) without completely reording the heap.
	
reachable(): lists all nodes reachable by each node

	Should be O(V*(|V|+|E|), every object is running a DFS so it is the length of a DFS (O(|V|+|E|) * 
	every node V. I took special care not to allow the sorting of the nodes into alphabetical order to 
	affect the run time. The sorting is done when the graph is set up and is simply marked down as visited 
	or not, then it is printed in order by iterating through each node. This takes O(V*(V+V+E)) time 
	instead of  O(V*(VlogV+E)) where logV is the assumed sort time of the built in sort function.


Main Data structures:

 Graph: 
 
	vd: Dictionary, stores all vertices in graph
	sort: List, stores all the keys (vertices) in alphabetical order
	sortAdj: Dictionary, stores all vertices and contains whether it is visited for the DFS in reachable()
	
 Graph.path() which runs Dijsktra's:
 
	e: Dictionary, stores a pointer to heapobj objects
	p: Dictionary, stores all vertices and the predicessor for each one
	minDist: Heap, stores a pointer to heapobj and is sorted as heap
	
 Vertex:
 
	adj: Dictionary, adjacent edges
 
 Heap:
 
	a: List, stores a pointer to heapobj sorted into heap format

Files: README.txt, network.txt, otherNetwork.txt, queries.txt, output.txt, graph.py, vertex.py, edge.py, heapobj.py, and minheap.py

	-You are reading the README
	-network.txt is the provide graph
	-otherNetwork.txt was used in much of my testing so I included it for reference.
	-queries.txt is the provide commands
	-output.txt is the provided output
	-graph.py is the Graph class and main class (run this one)
	-vertex.py is the Vertex class which represents each node
	-edge.py is the Edge class which represents each conenction
	-heapobj.py is the Heapobj class which is used by minheap.py
	-minheap.py is the Heap class which represents the shortest path and is used in graph.path()

Sucesses:

	-Was able to make a very usable software
	-Was able to hit the ideal run times. This took the most work.

Limitations:

	-Python stinks at pointers. It only emulates them through objects. Next time I would use another language.

Language:

	Python 3.6.2

Compiler:

	PyCharm 2017.2.3 

To Run: 

	run >>python graph.py networkFile.txt on the command line
	commands:
	addedge tailvertex headvertex trasmittime
	deleteedge tailvertex headvertex
	edgedown tailvertex headvertex
	edgeup tailvertex headvertex
	vertexdown vertex
	vertexup vertex
	path from_vertex to_vertex
	print
	reachable
	help
	quit
