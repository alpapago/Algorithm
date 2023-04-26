import sys
from collections import deque
input = sys.stdin.readline

n,k= map(int,input().split())
q = deque()
result = []

for i in range(1,n+1):
    q.append(i)

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())

print('<',end='')
for i in range(n-1):
    print(result[i],end=', ')
print(result[-1],end='')
print('>')