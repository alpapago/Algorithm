n,m=map(int,input().split(' '))
array=list(map(int,input().split(' ')))

max_value=-1
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = array[i]+array[j]+array[k]
            if sum<=m:
                max_value=max(max_value,sum)

print(max_value)