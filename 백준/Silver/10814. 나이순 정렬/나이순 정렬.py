n = int(input())

arr = []
for _ in range(n):
    data = input().split(' ')
    arr.append((int(data[0]),data[1]))

arr = sorted(arr, key=lambda x:x[0])

for i in arr:
    print(i[0], i[1])