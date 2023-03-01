from itertools import combinations

vowels = ('a','e','i','o','u')
l,c=map(int,input().split(' '))

array=input().split(' ')
array.sort() #사전식 암호를 만들어야 하므로.

for password in combinations(array,l):
    count=0 #모음 갯수 셀거임.
    for i in password:
        if i in vowels:
            count+=1
    if count>=1 and count <= l-2:
        print(''.join(password))