n = int(input())
arr = list(map(int,input().split()))
stack=[]
result=[-1]*n

for i in range(n):
    x=arr[i]
    if len(stack)==0  or stack[-1][0]>=x:
        stack.append((x,i))
    else:
        while len(stack)>0:
            previous, index =stack.pop()
            if previous >=x:
                stack.append((previous,index))
                break
            else:
                result[index]=x
        stack.append((x,i))

for x in result:
    print(x,end=' ')