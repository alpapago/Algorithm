#int 는 iterator가 안된다! str로 받고 index로 쓰고싶으면 int로 형변환하기.
#str은 인덱스로 접근도 가능하다. 
arr = input()

for i in range(9,-1,-1):
    for j in arr:
        if int(j) == i:
            print(i,end='')