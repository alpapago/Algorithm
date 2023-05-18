import sys
sys.setrecursionlimit(int(1e4))
input = sys.stdin.readline

n,k = map(int,input().split())
A = list(map(int,input().split()))


def quickSort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

def partition(A,p,r):
    global k
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j] = A[j],A[i]
            k-=1
            if k == 0:
                print(A[i], A[j])
                break

    if i+1!=r:
        A[i+1],A[r] = A[r],A[i+1]
        k-=1
        if k == 0:
            print(A[i+1], A[r])
            exit(0)
    return i+1

quickSort(A,0,len(A)-1)

if k>0:
    print(-1)