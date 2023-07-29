import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())):
    n = int(input())
    arr = []

    result = []

    for _ in range(n//10+1):
        arr.extend(list(map(int,input().split())))
    
    # 처음 중앙값
    mid = arr[0]
    # 첫번째 중앙값을 답에 일단 넣음
    result.append(mid)

    # 중앙값 양쪽 힙 만들기
    left = []
    right = []

    for i in range(1,n):
        if mid<arr[i]:
            heapq.heappush(right,arr[i])
        else:
            # 내림차순으로 정렬해주는 max_heap에 추가
            heapq.heappush(left,-arr[i])
        # mid 갱신해야됨.
        if not i%2: # 홀수번째 원소를 넣었을 때마다,
            if len(left) < len(right):
                heapq.heappush(left,-mid)
                mid = heapq.heappop(right)
            elif len(right) < len(left):
                heapq.heappush(right,mid)
                mid = -heapq.heappop(left)
            result.append(mid)
    
    print(len(result))
    for i in range(len(result)):
        print(result[i], end = ' ')
        if (i+1)%10 == 0:
            print()
    print()# 그 다음 케이스 줄바꿈.