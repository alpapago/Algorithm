n=int(input())

count=1
stack=[]
result=[]

for i in range(n):
    x = int(input())
    while count<=x:
        stack.append(count)
        result.append('+')
        count+=1
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)
            
print('\n'.join(result))