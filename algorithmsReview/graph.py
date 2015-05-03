class DirectedGraph(object):

    """ my impementation of a directed graph """

    def __init__(self):
        print "initialized graph"
        self.Adj = {}

    def addVertex(self, vertexKey,edges):
        self.Adj[vertexKey] = edges

    def addEdgeToVertex(self, vertexKey, edgeToAdd):
        self.Adj[vertexKey].append(edgeToAdd)

    def deleteEdgeFromVertex(self, vertexKey, edgeToDelete):
        self.Adj[vertexKey].remove(edgeToDelete)
