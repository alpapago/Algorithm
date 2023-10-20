
stack = []
result = []
now = 1

flag = True

A = []
n = int(input())

for i in range(n):
    A

for _ in range(n):


    if now < n:
        while True:
            stack.append(now)
            now += 1
            result.append('+')

        stack.pop()
        result.append('-')
    else:
        tmp = stack.pop()

        if tmp > n:
            flag = False
            print('NO')
            break

        else:

            result.append('-')

if flag:
    for i in result:
        print(i)
