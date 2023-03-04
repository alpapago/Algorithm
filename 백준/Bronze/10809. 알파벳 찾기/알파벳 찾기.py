import sys
input = sys.stdin.readline

arr = [-1]*26
data = input().strip()

for i in range(len(data)):
    index = ord(data[i])-ord('a')
    if arr[index]==-1:
        arr[index]=i

for j in arr:
    print(j, end=' ')