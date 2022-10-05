N, M = map(int, input().split())  # N M 입력 받기
rq = list(range(1, N+1))  # 1부터 N까지 자연수 리스트 생성
find = list(map(int, input().split()))  # 뽑아내려고 하는 수 리스트 입력 받기

count = 0  # 왼쪽이나 오른쪽으로 한 칸 이동되면 +1
for i in find:
    while True:
        if rq[0] == i:
            rq.pop(0)
            break
        else:
            if rq.index(i) < len(rq)/2: # 왼쪽으로 가는게 빠른지 오른쪽으로 가는게 빠른지 반 나눠서 판단
                while rq[0] != i:
                    rq.append(rq.pop(0)) # 가장 앞에 있는 요소 가장 뒤로 보내기
                    # rq.insert(-1, rq.pop(0))를 썼었는데 이렇게 하면 마지막 요소의 앞에 insert가 되어버린다
                    count += 1
            else:
                while rq[0] != i:
                    rq.insert(0, rq.pop(-1)) # 가장 뒤에 있는 요소 가장 앞으로 보내기
                    count += 1

print(count)

            

