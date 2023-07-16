tc = int(input())

result = []

for _ in range(tc):
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    # i : 중요도 / idx : 인덱스
    data = [(i,idx) for idx,i in enumerate(data)]

    cnt = 1
    while True:
        #뽑은 원소가 data배열 중에 중요도가 최대라면? pop해야지
        if data[0][0] == max(data,key=lambda x:x[0])[0]:
            #근데 원하는 index의 값이 아냐? 1번 카운트 하고 pop해야지
            if data[0][1] != m:
                cnt+=1
                data.pop(0)
            #원하는 인덱스야? 그러면 result에 추가해야지
            else:
                result.append(cnt)
                break
        #뽑은 원소가 data배열 중 중요도 최대값이 아니라면?
        else:
            #회전을 해야지
            data.append(data.pop(0))

for i in result:
    print(i)