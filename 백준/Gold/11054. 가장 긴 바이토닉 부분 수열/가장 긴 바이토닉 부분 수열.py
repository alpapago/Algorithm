import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
dp =[1]*n
dp2 =[1]*n

def ma(a,dp):
    for i in range(1,n):
        for j in range(i):
            if a[i] >a[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return dp

new1 = ma(a,dp)
b = a[::-1]
new2 = ma(b,dp2)
new22= new2[::-1]

k= [ new1[i]+new22[i] for i in range(len(new1))]
print(max(k)-1)