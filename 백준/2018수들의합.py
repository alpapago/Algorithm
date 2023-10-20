import sys
input = sys.stdin.readline

n = int(input())

start, end = 1, 1
tmpsum = start + end
cnt = 0

while end < n:

    if tmpsum == n:
        cnt += 1
        end += 1
        tmpsum += end
    # 합이 n보다 작으면,
    elif tmpsum < n:
        end += 1
        tmpsum += end
    # 합이 n보다 크면,
    elif tmpsum > n:
        tmpsum -= start
        start += 1

print(cnt)