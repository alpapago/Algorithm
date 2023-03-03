import sys
input = sys.stdin.readline
import heapq

k,n=map(int,input().split())
data = list(map(int,input().split()))
heap=[]
visited=set()
max_value= max(data)

for x in data:
    heapq.heappush(heap,x)

#n-1개 원소 꺼내기
for i in range(n-1):
    element= heapq.heappop(heap)
    for x in data:
        now = element*x
        if len(heap)>=n and max_value<now:
            continue
        if now not in visited:
            heapq.heappush(heap,now)
            visited.add(now)
            max_value=max(now, max_value)

print(heapq.heappop(heap))