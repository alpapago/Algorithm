import sys
input = sys.stdin.readline

arr =[]
sum = 0

for _ in range(5):
    n = int(input())
    arr.append(n)
    sum+=n

arr.sort()

print(sum//5)
print(arr[2])