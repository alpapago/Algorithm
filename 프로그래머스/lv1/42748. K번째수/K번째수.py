def solution(array, commands):
    answer = []

    for command in commands:
        answer.append(cut(array, command))

    return answer

def cut(array, command):
    #n 번째 수의 index는 n-1이므로
    i = command[0]-1
    j = command[1]-1
    k = command[2]-1

    #array 를 i 번째부터 j번째 원소까지 부분배열 생성
    tmp = [array[idx] for idx in range(i,j+1)]
    
    tmp.sort(reverse = False)

    return tmp[k]