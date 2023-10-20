import sys
input = sys.stdin.readline

n = int(input())
arr =list(map(int,input().split()))

arr.sort()

m = int(input())
arr2 = list(map(int,input().split()))

def midsearch(x, library ):
    mid = (0+len(library))//2

    while True:
        if library[mid] == x:
            return library[mid]


for i in arr2:
    mid