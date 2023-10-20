import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):

    q = deque([v])
    visited[v] = 1

    while q:
        now = q.popleft()

        for e in adj[now]:
            if not visited[e]:
                q.append(e)
                visited[e] = 1


n,d = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [0]*(n+1)

# 그래프 연결!!
for _ in range(d):
    a, b = map(int,input().split())

    # 무방향 그래프
    adj[a].append(b)
    adj[b].append(a)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
