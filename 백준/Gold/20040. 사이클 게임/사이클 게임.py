import sys
input =sys.stdin.readline

def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    x=find(parent,x)
    y=find(parent,y)

    if x<y:
        parent[y]=x
    else:
        parent[x]=y

n,m=map(int,input().split())
parent=[0]*n
for i in range(n):
    parent[i]=i

cycle=False
for i in range(m):
    a,b=map(int,input().split())
    if find(parent,a)==find(parent,b):
        cycle=True
        print(i+1)
        break
    else:
        union(parent,a,b)

if not cycle:
    print(0)