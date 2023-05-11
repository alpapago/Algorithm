import heapq

n = int(input())

arr = []

for _ in range(n):
    arr.append(-int(input()))

heap = []

for i in arr:
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap,i)