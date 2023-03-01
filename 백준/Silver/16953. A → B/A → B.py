import sys
input = sys.stdin.readline
from collections import deque

s,t = map(int,input().split())
queue =deque([])
queue.append((s,0))
visited= set()
found=False
while len(queue)!=0:
    value, dist =queue.popleft()
    if value > int(1e9):
        continue
    if value ==t:
        print(dist+1)
        found =True
        break
    for oper in ['*','+']:
        next_value =value
        if oper =='*':
            next_value*=2
        if oper =='+':
            next_value*=10
            next_value+=1
        if next_value not in visited:
            queue.append((next_value,dist+1))
            visited.add(next_value)
if not found:
    print(-1)