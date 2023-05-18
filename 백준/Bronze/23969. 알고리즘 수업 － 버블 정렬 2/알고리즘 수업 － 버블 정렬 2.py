import sys
input = sys.stdin.readline

def bubbleSort(A):
    cnt = 0
    for last in range(len(A)-1,0,-1):
        for i in range(last):
            if A[i]>A[i+1]:
                cnt += 1
                tmp = A[i]
                A[i] = A[i+1]
                A[i+1] = tmp
                if cnt == k:
                    pnt(A)
                    break 
    if cnt < k:
        print(-1)

def pnt(A):
    for i in A:
        print(i,end=' ')
    
n,k = map(int,input().split())
A = list(map(int,input().split()))

bubbleSort(A)