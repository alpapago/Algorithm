import sys
input = sys.stdin.readline

def find(parent,x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
        
    return parent[x]


def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int,input().split())
parent = [i for i in range(n+1)]

answer = 1

for _ in range(m):
    a, b = map(int, input().split())
    union(parent,a,b)

cnt = set()
for i in range(1,n+1):
    cnt.add(find(parent,i))

print(len(cnt))