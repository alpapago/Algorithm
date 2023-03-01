import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
m=int(input())

graph =[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance=[-1]*(n+1)
distance[1]=0

queue = deque([1])
while queue:
    x=queue.popleft()
    for y in graph[x]:
        if distance[y]==-1:
            distance[y]=distance[x]+1
            queue.append(y)

result = 0
for i in range(1,n+1):
    if distance[i] != -1 and distance[i]<=2:
        result+=1
print(result-1)