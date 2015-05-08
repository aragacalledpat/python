from graph import DirectedGraph

class BreadthFirstSearch:
    def __init__(self, graph, s):
        print "init breadth first search"
        self.bfs(graph, s)

    def bfs(self, graph, s):
        print "lets do this"

testGrapth = DirectedGraph()
testGrapth.addVertex("b",["a", "c"])
testGrapth.addVertex("a",["c"])
testGrapth.addVertex("c",["b"])



test = BreadthFirstSearch(testGrapth,"a")
