T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)] #나무가 심어지는 배열 arr을 만듭니다.
    sm = 0
    for i in range(N):
        for j in range(0, M, 2): #j의 범위는 0부터 M까지 2씩 증가합니다.
            sm += arr[i][j] #나무를 심는 총 비용입니다.

    a = N * ((M+1)//2) #심은 나무 수 입니다.
    cnt = 0
    t = 0
    for i in range(N):
        for j in range(0, M, 2):
            if cnt <= arr[i][j]: #배열 범위 내에서 가장 비싼 나무의 가격을 구해줍니다. 이 때 =을 추가한 이유는
                cnt = arr[i][j]  #가장 비싼 나무의 가격이 같다면 뒤쪽의 것을 출력해야하기 때문입니다.
                t = j #가장 비싼 나무의 열을 구합니다. 이때 범위가 0부터 시작하기에 출력시 1을 더해야합니다.

    print(f'#{tc} {sm} {a} {cnt} {t+1}')