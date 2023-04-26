import sys
from collections import deque
input = sys.stdin.readline

q=deque()

n=int(input())

for _ in range(n):
    x=input().split()
    if x[0]=='push_front':
        q.appendleft(x[1])
    elif x[0]=='push_back':
        q.append(x[1])
    elif x[0]=='pop_front':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif x[0]=='pop_back':
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif x[0]=='size':
        print(len(q))
    elif x[0]=='empty':
        if not q:
            print(1)
        else:
            print(0)
    elif x[0]=='front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif x[0]=='back':
        if not q:
            print(-1)
        else:
            print(q[-1])