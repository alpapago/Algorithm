import sys
input =sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    arr = list(map(int,input().split()))

    max_val = arr[n-1] #가장 마지막 원소
    sell=[0]*n #팔 가격
    #뒤쪽부터 거꾸로 확인.
    for i in range(n-1,-1,-1): #마지막원소부터 처음 원소까지 거꾸로.
        max_val = max(max_val,arr[i])
        sell[i]=max_val

    result =0
    for i in range(n):
        #이익이 생길때만 더해주는거래..
        result += max(0,sell[i]-arr[i])
    print(result) 