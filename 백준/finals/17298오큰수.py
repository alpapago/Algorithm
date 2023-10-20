n = int(input())
arr = list(map(int,input().split()))

result = []
stack = []

# 거꾸로 인덱싱
for i in range(n-1,-1,-1):
    tmp = arr[i]

    while True:

        if not stack:
            stack.append(tmp)
            result.append(-1)
            break
        elif stack[-1] > tmp:
            result.append(stack[-1])
            stack.append(tmp)
            break
        else:
            stack.pop()

result.reverse()
for i in result:
    print(i,end=' ')
