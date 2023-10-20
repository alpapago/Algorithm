import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

# 투포인터 써야하니까 sort
A.sort()

# 전체 해답
cnt = 0

for i in range(n):

    # 현재 수
    find = A[i]

    # 인덱스
    start, end = 0, n - 1

    while start < end:

        if find == A[start] + A[end]:
            if start != i and end != i:
                cnt += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1

        elif find > A[start] + A[end]:
            start += 1

        elif find < A[start] + A[end]:
            end -= 1

print(cnt)