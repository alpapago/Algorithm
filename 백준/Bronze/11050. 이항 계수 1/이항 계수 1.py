import sys
input = sys.stdin.readline

n,k = map(int,input().split())

def fac(n):
    if n ==0 or n==1:
        return 1
    elif n>1:
        return n*fac(n-1)

answer = fac(n)//(fac(n-k)*fac(k))

print(answer)