n = int(input())

arr=[]

for _ in range(n):
    a,b=input().split()
    arr.append((int(a),b))

arr.sort(lambda x:x[0])

for i in arr:
    print(i[0],i[1])