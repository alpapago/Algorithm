import sys
input = sys.stdin.readline

def selectionSort(A):
    cnt = 0
    for last in range(len(A)-1,0,-1):
        m = largest(A,last)
        if last != m:
            cnt+=1
            A[m],A[last] = A[last],A[m]
            if k == cnt:
                for i in A:
                    print(i,end=' ')
    if cnt<k:
        print(-1)

def largest(A,last):
    lar = 0
    for i in range(last+1):
        if A[i] > A[lar]:
            lar = i
    return lar


n, k = map(int,input().split())
A = list(map(int,input().split()))

selectionSort(A)