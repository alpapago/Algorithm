import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

#무방향 그래프의 경우는 prev가 중요하다.
def is_cycle(x,prev):
    visited[x]=True
    #x의 인접노드 y의 경우에
    for y in graph[x]:
        if visited[y]: #y를 방문했었고, 직전노드가 아니면,
            if y!=prev:
                return True
        else:#방문 안한 y가 나타났다?
            if is_cycle(y,x):
                return True # 재귀로 사이클 찾기.
    #사이클이 되는 모든 경우의 수 다 살펴봤는데, 아니다?
    return False

test_case=1
while True:
    n,m=map(int,input().split())
    if n == 0 and m == 0:
        break
    graph=[[] for _ in range(n+1)]
    visited=[False]*(n+1)

    for i in range(m):#간선 갯수 만큼 이동 및 input을 넣을거임.
        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    cnt =0 #트리갯수 저장 변수. 사이클 아닌거 찾기.
    for i in range(1, n+1):#dfs돌릴때는 1번 노드 부터 가면된다. 
        if not visited[i]:
            if not is_cycle(i,0):
                cnt+=1
    
    if cnt==0:
        print(f'Case {test_case}: No trees.')
    elif cnt==1:
        print(f'Case {test_case}: There is one tree.')
    else:
        print(f'Case {test_case}: A forest of {cnt} trees.')
    test_case+=1