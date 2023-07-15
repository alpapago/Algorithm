from collections import deque

n,k = map(int, input().split())
data = deque([i for i in range(1,n+1)])

result = []

while len(data)!=0:
    for i in range(k-1):
        data.append(data.popleft())
    result.append(data.popleft())

print('<',end='')
for i in range(len(result)-1):
    print(result[i],end=', ')

print(result[-1],end='>')