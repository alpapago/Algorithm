import sys
input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):

    n, k = map(int, input().split(' '))
    arr = list(map(int, input().split(' ')))
    q = [(i,idx) for idx,i in enumerate(arr)]

    cnt = 0

    while True:
        if q[0][0] == max(q,key = lambda x:x[0])[0]: #배열을 큐 처럼 사용. 우선순위 젤 높은거 찾기.
            cnt+=1 #우선순위가 젤 높아서 일단 해당원소를 빼야하니까 카운트 1회
            #근데 인덱스가 k값이 맞는지 확인
            if q[0][1] == k:
                print(cnt)
                break #정답 프린트 하고 종료
            else:
                #인덱스가 k값 아니라도 popleft는 해야함.
                q.pop(0)
        else: #우선순위 젤 높지 않다면,
            #뱅글뱅글
            q.append(q.pop(0))