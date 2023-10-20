n = int(input())
gap = int(input())

data = list(map(int,input().split()))
data.sort()

result = 0

start, end = 0, n - 1

while start < end:
    tmp = data[start]+data[end]
    # tmp가 gap이랑 같나
    if tmp == gap:
        result += 1
        start += 1

    elif tmp < gap:
        start += 1

    elif tmp > gap:
        end -= 1

print(result)