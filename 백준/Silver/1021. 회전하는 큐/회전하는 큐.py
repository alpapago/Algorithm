from collections import deque
import sys
input = sys.stdin.readline

n , m = map(int, input().split())
q = deque([i for i in range(1,n+1)]) 
elements = list(map(int,input().split()))
cnt = 0

for element in elements:
    index = q.index(element)

    #원소가 2n개면, index = n(2n//2와 같다.) 인 요소는 앞으로 돌리나 뒤로 돌리나 상관없다.
    #원소가 2n-1개면, index = n-1(2n-1//2와 같다.)인 요소를 기준으로 왼쪽 오른쪽 나뉜다.

    if index<=len(q)//2:
        for i in range(index):
            q.append(q.popleft())
            cnt+=1
    else:
        for i in range(len(q)-index):
            q.appendleft(q.pop())
            cnt+=1
    
    #인덱스 만큼 이동해서 해당 원소를 찾은 후,

    q.popleft()

print(cnt)