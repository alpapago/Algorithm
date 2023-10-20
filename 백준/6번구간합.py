import sys
input = sys.stdin.readline

n,m = map(int,input().split())
numlist = list(map(int,input().split()))

sumlist = [0]


tmp = 0
# sumlist 만들기
for i in range(n):
    tmp += numlist[i]
    sumlist.append(tmp)


for _ in range(m):
    s_idx, e_idx = map(int,input().split())
    print(sumlist[e_idx]-sumlist[s_idx-1])
