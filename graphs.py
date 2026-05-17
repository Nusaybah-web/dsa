class graphs:
    def __init__(self,vertecis):
        self.graph=[]
        for i in range(vertecis):
            self.graph.append([])
    def addedge(self,u,b):
        self.graph[u].append(b)
        self.graph[b].append(u)
    def bfs(self,start):
        visited=[]
        queue=[]
        for i in range(len(self.graph)):
            visited.append(False)
        queue.append(start)
        visited[start]=True
        while queue:
            current=queue.pop(0)
            print(current)
            for i in self.graph[current]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

g=graphs(5)
g.addedge(0,1)
g.addedge(1,2)
g.addedge(2,4)
g.addedge(3,4)

print("bfs triversal", g.bfs(0))