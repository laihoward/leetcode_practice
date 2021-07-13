graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"],
}

def BFS(graph,s):
    queue=[]
    queue.append(s)
    seen=set() #seen為集合
    seen.add(s) #集合加入值用add
    parent = {s:None}
    while len(queue)>0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
                parent[i] =vertex
        print(vertex)
    return parent

def DFS(graph,s):
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

# BFS(graph,"A")
# print(BFS(graph,"A"))
parent = BFS(graph,"A")
v="F"
print("="*5)
while v!=None:
    print(v)
    v=parent[v]