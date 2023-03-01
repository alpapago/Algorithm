import sys
input=sys.stdin.readline
from collections import deque

def bfs(x):
    queue = deque([x])
    visited[x]=0
    while queue:
        x=queue.popleft()
        for y in graph[x]:
            if visited[y]==-1:
                visited[y]=(visited[x] +1)%2
                queue.append(y)
    
def is_bipartite():
    for x in range(1,v+1):
        for y in graph[x]:
            if visited[x]==visited[y]:
                return False
    return True

for _ in range(int(input())):
    v,e = map(int,input().split())
    graph=[[] for _ in range(v+1)]
    for i in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[-1]*(v+1)
    for x in range(1,v+1):
        if visited[x]==-1:
            bfs(x)
            
    if is_bipartite():print("YES")
    else: print("NO")