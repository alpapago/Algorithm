import sys
import heapq

input = sys.stdin.readline

# 1 ~ n 까지 수, m : 먼저 풀면 좋은 문제 수
n, m = map(int, input().split())
board = [[] for _ in range(n + 1)]
phase = [0 for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    phase[b] += 1

# input 간선이 0개로, 위상이 가장 높은 vertex를 priority queue에 삽입
q = []
for i in range(1, n + 1):
    if phase[i] == 0:
        heapq.heappush(q, i)

answer = []

while q:
    now = heapq.heappop(q)
    answer.append(now)
    for i in board[now]:
        if phase[i] == 0:
            continue
        else:
            phase[i] -= 1
            if phase[i] == 0:
                heapq.heappush(q, i)

print(*answer)
