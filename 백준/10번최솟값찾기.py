import sys
input = sys.stdin.readline
from collections import deque

n, l = map(int, input().split())
nowdeque = deque()
now = list(map(int,input().split()))

for i in range(n):
    # 인덱스 , 숫자
    while nowdeque and nowdeque[-1][0] > now[i]:
        nowdeque.pop()
    nowdeque.append((now[i], i))
    if nowdeque[0][1] <= i-l:
        nowdeque.popleft()
    print(nowdeque[0][0], end = ' ')