import sys
input = sys.stdin.readline

def selectionSort(A, k):
    cnt = 0
    for last in range(len(A)-1,0,-1): #마지막 인덱스부터 1까지
        m = largest(A, last) #[0,...,last] 중, 제일 큰 m찾기
        if last != m:
            A[m],A[last] = A[last],A[m]
            cnt += 1
            if cnt == k:
                print(A[m], A[last])
                break
    if cnt < k:
        print(-1)

def largest(A, last):
    lar = 0
    for i in range(last+1):
        if A[i] > A[lar]:
            lar = i
    return lar #인덱스를 리턴

n,k = map(int, input().split())
A = list(map(int,input().split(' ')))

selectionSort(A, k)