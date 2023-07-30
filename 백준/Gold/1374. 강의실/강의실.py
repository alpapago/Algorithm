import sys
input = sys.stdin.readline
import heapq

classes = []

# 데이터 input
for _ in range(int(input())):
    n, start,end = map(int,input().split())
    heapq.heappush(classes,(start,end))

# 강의실 갯수를 세어보자
# 일단 제일 빨리 시작하는 강의를 꺼내서 끝나는 시간 check
cnt = [heapq.heappop(classes)[1]]

# n-1개의 class를 강의실에 다 배정 > 끝나는 시간만 저장
for i in range(n-1):
    end = heapq.heappop(cnt)
    new_start,new_end = heapq.heappop(classes)
    if end > new_start:
        heapq.heappush(cnt,end)
        heapq.heappush(cnt,new_end)
    else:
        heapq.heappush(cnt,new_end)

print(len(cnt))