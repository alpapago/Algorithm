from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    f = input().strip()
    n = int(input())
    arr = input().strip()
    d = deque(arr[1:-1].split(','))

    flag = 1 # 길이 0일때 문제 안생기게!

    if n == 0:
        d = deque() #길이가 0이면 빈 덱 리턴
    #R 갯수가 홀수개면 뒤집기 해주어야하므로 R갯수 인덱스 만들기
    R = 0
    for i in range(len(f)):
        if f[i] == 'R':
            R +=1
        elif f[i] == 'D':
            if len(d) == 0:
                print('error')
                flag = 0
                break
            else:
                if R%2 ==0:
                    d.popleft()
                else:
                    d.pop()
    
    if flag == 0:
        continue

    else:
        if R % 2 == 0:
            print('[' + ",".join(d) + ']')
        else:
            d.reverse()
            print('[' + ",".join(d) + ']')