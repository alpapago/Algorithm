doc = input()
word = input()

index =0 
result =0

while len(doc)-index>=len(word):
    if doc[index:index+len(word)]==word:
        result +=1
        index+=len(word)
    else:
        index+=1

print(result)