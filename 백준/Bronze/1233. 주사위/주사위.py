a,b,c = map(int,input().split())

result = [0 for _ in range(a+b+c+1)]

#합 구하기
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            result[i+j+k] +=1

result = [(i,idx) for idx,i in enumerate(result)]

result.sort(key= lambda x:x[0],reverse=True)

print(result[0][1])