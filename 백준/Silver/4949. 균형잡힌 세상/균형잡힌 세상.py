while True:
    a = input()
    stack = []

    if a =='.':
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if stack and stack[-1] == '[' :
                stack.pop() 
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if not stack:
        print('yes')
    else :
        print('no')