import sys
input= sys.stdin.readline

stack=[]

n=int(input())
for _ in range(n):
    command=input().split()
    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if not len(stack):
            print(-1)
        else:
            print(stack.pop())
    elif command[0]=='size':
        print(len(stack))
    elif command[0]=='empty':
        if not len(stack):
            print(1)
        else: print(0)
    else:
        if not len(stack):
            print(-1)
        else: print(stack[-1])