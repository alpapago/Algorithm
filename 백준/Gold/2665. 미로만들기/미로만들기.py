import sys
input = sys.stdin.readline
import heapq

n=int(input())
graph=[[0]*n for _ in range(n)]

for i in range(n):
    row=input()
    for j in range(n):
        graph[i][j] = int(row[j])

dx=[-1,1,0,0]
dy=[0,0,-1,1]

visited=[[-1]*n for _ in range(n)]

queue =[]
#(검은방 없앤 횟수, x,y) 를 queue에 삽입
heapq.heappush(queue,(0,0,0))
visited[0][0]=0

while queue:
    count, x,y = heapq.heappop(queue)
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        #방문하지 않은 점이라면,
        if visited[nx][ny]==-1:
            #검은방인 경우 카운트를 증가해서 삽입.
            if graph[nx][ny]==0:
                visited[nx][ny]=count+1
                heapq.heappush(queue,(count+1,nx,ny))
            #흰방인 경우 카운트를 그대로 삽입.
            else:
                visited[nx][ny]=count
                heapq.heappush(queue,(count,nx,ny))

print(visited[n-1][n-1])