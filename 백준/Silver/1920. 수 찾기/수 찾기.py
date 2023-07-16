import sys
input = sys.stdin.readline

a = int(input())
sett = set(map(int,input().split( ))) #중복 없이 자료 저장해줌.
b = int(input())
listt = list(map(int,input().split( )))

for i in listt:
    if i not in sett:
        print("0")
    else:
        print("1")