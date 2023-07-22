n = int(input())
data = list(map(int,input().split(' ')))

result = [-1]
stack = [data[-1]]

for i in range(len(data)-2,-1,-1):
    while True:
        if len(stack) == 0:
            result.append(-1)
            stack.append(data[i])
            break
        else:
            if data[i] < stack[-1]:
                result.append(stack[-1])
                stack.append(data[i])
                break
            else:
                stack.pop()

result.reverse()

for i in result:
    print(i,end = ' ')