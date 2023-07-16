s = input()

num = [0 for i in range(10)]

for i in range(len(s)):
    num[int(s[i])] +=1

for i in range(9,-1,-1):
    for j in range(num[i]):
        print(i,end='')