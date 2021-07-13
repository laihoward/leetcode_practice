import heapq
import math
class graphdis(object):
    def BFS(self,graph,s):
        queue=[]
        queue.append(s)
        seen=set() #seen為集合
        seen.add(s) #集合加入值用add
        parent = {s:None}#紀錄每個node的前一個node
        while len(queue)>0:
            vertex = queue.pop(0)
            nodes = graph[vertex]
            for i in nodes:
                if i not in seen:
                    queue.append(i)#queue加入還沒存在set中的node
                    seen.add(i)#將還沒存在set中的node存入set
                    parent[i] =vertex
            print(vertex)
        return parent

    def DFS(self,graph,s):
        stack=[]
        stack.append(s)
        seen=set() #seen為集合
        seen.add(s) #集合加入值用add
        parent = {s:None}
        while len(stack)>0:
            vertex = stack.pop()
            nodes = graph[vertex]
            for i in nodes:
                if i not in seen:
                    stack.append(i)
                    seen.add(i)
                    parent[i] =vertex
            print(vertex)
        return parent

    def init_distance(self,graph,s):#初始化距離
        distance = {s:0}
        for vertex in graph:
            if vertex != s:
                distance[vertex]=math.inf
        return distance

    def dijkstra(self,graph,s):#加上距離
        pqueue = []
        heapq.heappush(pqueue,(0,s))
        seen=set() #seen為集合
        parent = {s:None}#紀錄每個node的前一個node
        distance=self.init_distance(graph,s)#node到起始點的距離
        while len(pqueue)>0:
            pair = heapq.heappop(pqueue)
            dist = pair[0]
            vertex = pair[1]
            seen.add(vertex)
            nodes = graph[vertex].keys()
            for i in nodes:
                if i not in seen:
                    if dist + graph[vertex][i]<distance[i]:
                        heapq.heappush(pqueue,(dist + graph[vertex][i],i))
                        parent[i] =vertex
                        distance[i] = dist + graph[vertex][i]
            
        return parent,distance

graph = {
    "A":{"B":5,"C":1},
    "B":{"A":5,"C":2,"D":1},
    "C":{"A":1,"B":2,"D":4,"E":8},
    "D":{"B":1,"C":4,"E":3,"F":6},
    "E":{"C":8,"D":3},
    "F":{"D":6},
}
g = graphdis()
# parent = g.BFS(graph,"A")
# v="F"
# print("="*5)c
# while v!=None:
#     print(v)
#     v=parent[v]
parent,distance = g.dijkstra(graph,"A")
print(parent)
print(distance)
