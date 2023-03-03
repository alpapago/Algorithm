import sys
input = sys.stdin.readline
from collections import deque

n,m=map(int, input().split())
d=deque([i for i in range(1,n+1)]) #[1,2,3,4,5,...,n]
targets = list(map(int,input().split()))
cnt=0

for target in targets:
    index = d.index(target)
    #이건 돌리는 거고
    if index<=len(d)//2:
        for i in range(index):
            x=d.popleft()
            d.append(x)
            cnt+=1
    else:
        for i in range(len(d)-index):
            x=d.pop()
            d.appendleft(x)
            cnt+=1
    #이건 빼내는 거고
    d.popleft()

print(cnt)