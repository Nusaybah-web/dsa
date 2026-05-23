class graph:
    def __init__(self,vertecies):
        self.vertecies=vertecies
        self.adj=[[] for i in range(vertecies)]
    def addedge(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    def dfs(self,node,target,visited):
        print("visiting",node)
        visited[node]=True
        if node==target:
            print("target found")
            return True
        #visit neighbours
        for i in self.adj[node]:
            if visited[i]==False:
                found=self.dfs(i,target,visited)
                if found==True:
                    return True
        return False

g=graph(5)

g.addedge(2,3)
g.addedge(2,4)
g.addedge(4,1)
g.addedge(1,0)

visited=[False]*5
g.dfs(0,3,visited)