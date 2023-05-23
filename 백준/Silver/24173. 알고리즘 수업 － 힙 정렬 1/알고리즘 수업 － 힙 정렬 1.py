import sys
input = sys.stdin.readline

n,cnt= map(int,input().split())
A = list(map(int,input().split()))


def heapSort(A):
    global n
    global cnt
    buildMinHeap(A,n)
    for i in range(n,1,-1):
        A[0],A[i-1] = A[i-1],A[0]
        cnt-=1
        if cnt == 0:
            print(A[i-1], A[0])
            break
        heapify(A,0,i-1)
        

def buildMinHeap(A,n):
    #마지막 노드 찾아서 heapify
    for i in range(n//2-1,-1,-1):
        heapify(A,i,n)

def heapify(A,k,n):
    global cnt
    left = 2*k+1
    right = 2*k+2
    smaller = 0
    #인덱스 둘 다 있을 때, leaf중에 최솟값 찾기
    if right<n:
        if A[left]<A[right]:
            smaller = left
        else:
            smaller = right
    #왼쪽 리프노드만 취할것.
    elif left<n:
        smaller = left
    #재귀 끝내는거! 이 줄을 삭제하면 안된다.
    else:
        return

    #리프랑 부모노드랑 크기 비교
    if A[smaller]<A[k]:
        A[k],A[smaller] = A[smaller],A[k]
        cnt-=1
        if cnt == 0:
            print(A[k], A[smaller])
            return
        elif cnt<0:
            return
        heapify(A,smaller,n)

heapSort(A)

if cnt>0:
    print(-1)