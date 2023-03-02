def union(x,y):
    x = find(x)
    y = find(y)

    if x!=y:
        parent[y]=x
        number[x]+=number[y]

def find(x):
    if x == parent[x]:
        return x
    else:
        p=find(parent[x])
        parent[x]=p
        return parent[x]


tc = int(input())

for _ in range(tc):
    parent=dict()
    number=dict()

    n= int(input())

    for _ in range(n):
        x,y = input().split(' ')
        
        if x not in parent:
            parent[x]=x
            number[x]=1
        if y not in parent:
            parent[y]=y
            number[y]=1
    
        union(x,y)
        print(number[find(x)])