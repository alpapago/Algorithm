s = input()

result =  []

for i in range(97,123):
    if chr(i) in s:
        result.append(s.index(chr(i)))
    else:
        result.append(-1)

for i in result:
    print(i,end=' ')
    