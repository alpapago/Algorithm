import sys
input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    result =1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<=-1 or nx>=n or ny<=-1 or ny>=n:
            continue
        if graph[nx][ny]==1:
            graph[nx][ny] = -1 #방문처리
            result += dfs(nx,ny)
    return result

n = int(input())
graph =[[0]*n for _ in range(n)]

for i in range(n):
    row= input() #list
    for j in range(n):
        graph[i][j]=int(row[j])

answer=[]

for i in range(n):
    for j in range(n):
        if graph[i][j] ==1:
            graph[i][j]=-1
            answer.append(dfs(i,j))

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])