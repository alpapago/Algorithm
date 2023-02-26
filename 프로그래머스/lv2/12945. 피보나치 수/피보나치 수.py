def solution(n):
    answer = 0
    b=1
    while n!=0:
        answer,b = b,answer+b
        n-=1
        
    answer = answer%1234567
    
    return answer