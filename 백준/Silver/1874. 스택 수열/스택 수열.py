n = int(input())

result = []
stack = []
i = 1

for _ in range(n):
    num = int(input())

    while i<=num:
        stack.append(i)
        result.append('+')
        i+=1
    if num == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))