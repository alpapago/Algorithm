import sys
input = sys.stdin.readline

n = int(input())

arr =[0]*10001

for _ in range(n):
    x = int(sys.stdin.readline())
    arr[x] +=1

#데이터 연산 횟수가 10,000,000회나 되므로, 계수정렬 써야한다. 

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)