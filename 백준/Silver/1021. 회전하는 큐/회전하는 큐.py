from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = deque([i for i in range(1,n+1)]) #1 부터 n까지 input
elements = list(map(int,input().split())) #숫자 인풋 받아서 배열로 만들기
cnt = 0

for element in elements:
    index = d.index(element)
   
    #원소가 홀수든 짝수든, index <= n/2 면 왼쪽 한 칸 이동시키는게 맞다
    #해당 element찾을때까지 자꾸 순환
    if index <= len(d)//2:
        for i in range(index):
            d.append(d.popleft())
            cnt+=1
    else:
        for i in range(len(d)-index):
            d.appendleft(d.pop())
            cnt+=1
    #element랑 같은 원소 찾으면, 뽑자
    d.popleft()

print(cnt)