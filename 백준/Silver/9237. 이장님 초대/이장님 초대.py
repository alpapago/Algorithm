import sys
input = sys.stdin.readline
n= int(input())
arr = list(map(int,input().split()))

arr.sort(reverse=True)
max_value=0
for i in range(n):
    max_value= max(max_value, i+1+arr[i])
print(max_value+1)