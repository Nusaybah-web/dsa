class graph:
    def __init__(self,vertecies):
        self.vertecies=vertecies
        self.adj=[[] for i in range(vertecies)]
    
    def store(self,temp,v,visited):
        visited[v]=True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i]==False:
                temp=self.store(temp,i,visited)
        return temp
    def addedge(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    #funtion to find all connected groups
    def connected(self):
        visited=[]
        cc=[]
        for i in range(self.vertecies):
            visited.append(False)
        for v in range(self.vertecies):
            if visited[v]==False:
                temp=[]
                cc.append(self.store(temp,v,visited))
        return cc

g=graph(5)

g.addedge(0,1)
g.addedge(2,3)
g.addedge(3,4)

print(g)

cc=g.connected()

print(cc)