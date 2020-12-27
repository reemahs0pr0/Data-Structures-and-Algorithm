import collections

def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for vertex in graph[start]:
        if vertex not in visited:
            dfs(graph, vertex, visited)

def bfs(graph, start):
    print("BFS: ",end="")
    seen = set([start])
    queue = collections.deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
    print()

graph = { 
    6 : set([73, 7]),
    73 : set([6, 23, 41]),
    7 : set([81, 62, 100]),
    23 : set([73, 69]),
    41 : set([73, 81, 69]),
    69: set([23, 41, 72]),
    81: set([7, 62, 72, 41]),
    72: set([69, 81, 20, 55]),
    100: set([7, 97]),
    62: set([81, 7, 97, 20]),
    97: set([62, 100, 82]),
    20: set([62, 82, 72]),
    82: set([97, 20, 55]),
    55: set([72, 82])
}

bfs(graph, 6)
print("DFS: ", end="")
dfs(graph, 6)