import sys
input = sys.stdin.readline

def insertionSort(A):
    cnt = 0
    for i in range(1,len(A)):
        loc = i-1
        newItem = A[i]
        while loc>=0 and A[loc]>newItem:
            A[loc+1] = A[loc]
            cnt += 1
            if cnt == k:
                for i in A:
                    print(i,end = ' ')
            loc -= 1
        if loc + 1 != i:
            A[loc+1] = newItem
            cnt += 1
            if cnt == k:
                for i in A:
                    print(i,end = ' ')
    
    if cnt < k:
        print(-1)

n,k = map(int,input().split())
A = list(map(int,input().split()))

insertionSort(A)