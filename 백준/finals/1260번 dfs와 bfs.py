import sys
input = sys.stdin.readline
from collections import deque

n,m,v = map(int,input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())

    adj[a].append(b)
    adj[b].append(a)

# 오름차순으로 방문한대.
for i in adj:
    i.sort()

def dfs(v):
    global res
    # 방문 처리
    visited[v] = 1

    res.append(v)

    for e in adj[v]:
        if not visited[e]:
            dfs(e)

def bfs(v):
    ans = []

    q = deque([v])
    visited[v] = 1

    while q:
        now = q.popleft()
        ans.append(now)
        for e in adj[now]:
            if not visited[e]:
                visited[e] = 1
                q.append(e)

    return ans

res = []
visited = [0]*(n+1)
dfs(v)

for i in res:
    print(i,end=' ')

print()

visited = [0]*(n+1)
result = bfs(v)
for i in result:
    print(i,end=' ')
