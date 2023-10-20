import sys
input = sys.stdin.readline

def find(x):

    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(q,w):
    q = find(q)
    w = find(w)

    if q != w:
        parent[q] = w
        number[w] += number[q]


for i in range(int(input())):
    n = int(input())
    parent = dict()
    number = dict()

    for _ in range(n):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            number[a] = 1

        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a,b)

        print(number[find(a)])