import sys

m = int(sys.stdin.readline())
graph = {}
for i in range(m):
    a, b, c = sys.stdin.readline().split()
    if a not in graph:
        graph[a] = []
    graph[a].append(c)
    

n = int(sys.stdin.readline())
for i in range(n):
    f, b, t = sys.stdin.readline().split()

    nv = [f]
    v = set()
    p = False
    while nv:
        node = nv.pop()
        
        if node == t:
            p = True 

        if node not in v:
            v.add(node)
            if node in graph:
                nv.extend(graph[node])

    print("T" if p else "F")