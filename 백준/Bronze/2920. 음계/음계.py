a = list(map(int,input().split(' ')))

ascending = True
descending = True

for i in range(len(a)-1):
    if a[i] <= a[i+1]:
        descending = False
    else:
        ascending = False

if descending:
   print("descending")
elif ascending:
    print("ascending") 
else:
    print("mixed")