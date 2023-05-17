import sys
input = sys.stdin.readline

def mergesort(A):
    if len(A) == 1:
        return A

    q = (len(A)+1)//2
    leftArr = mergesort(A[:q])
    rightArr = mergesort(A[q:])
    return merge(leftArr,rightArr)

def merge(left,right):
    i = 0
    j = 0
    tmp = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            tmp.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            answer.append(right[j])
            j += 1

    while i<len(left): #왼쪽 부분 배열이 남은 경우
        tmp.append(left[i])
        answer.append(left[i])
        i+=1

    while j<len(right): #오른쪽 부분 배열이 남은 경우
        tmp.append(right[j])
        answer.append(right[j])
        j+=1
    
    return tmp


n , k = map(int,input().split())
A = list(map(int, input().split(' ')))

answer = [] #static 배열
mergesort(A)

if k <= len(answer):
    print(answer[k-1])
else:
    print(-1)