import sys
input = sys.stdin.readline

def find(parent,x):
    if parent[x]!=x:
        parent[x]=find(parent,parent[x])
    return parent[x]
    
def union(parent,a,b):
    a=find(parent,a)
    b=find(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i

for i in range(m):
    a,b=map(int,input().split())
    union(parent,a,b)

counter=set()
for i in range(1,n+1):
    counter.add(find(parent,i))

print(len(counter))