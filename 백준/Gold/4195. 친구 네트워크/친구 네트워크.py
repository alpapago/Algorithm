def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]
    
def union(x,y):
    x = find(x)
    y = find(y)

    if x!=y:
        parent[y] = x
        number[x] += number[y]

    

t = int(input())

for _ in range(t):
    
    parent = dict()
    number = dict()
    
    k = int(input())

    for _ in range(k):
        name1,name2 = input().split(' ')
        
        if name1 not in parent:
            parent[name1] = name1
            number[name1] = 1
        if name2 not in parent:
            parent[name2] = name2
            number[name2] = 1
        
        union(name1,name2)

        print(number[find(name1)])