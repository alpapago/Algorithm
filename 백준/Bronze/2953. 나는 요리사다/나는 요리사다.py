
max_value =0
result=0
for i in range(1,6):
    arr = list(map(int,input().split(' ')))
    sum_val = sum(arr)
    if max_value<sum_val:
        max_value=sum_val
        result = i
    
print(result,max_value)