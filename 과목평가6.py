# 1번
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    bits = int(input(),16)

    cnt = ans = 0
    for i in range(4*N):
        if bits & (1<<i):
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt=0

    print(f'#{test_case} {ans}')


# 2번

def dfs(n, sm, cur):
    global ans
    if ans<=sm:
        return

    if n==N:
        if v[A]<v[B]:
            ans = min(ans, sm+arr[cur][0])
        return

    for j in range(1, N):
        if v[j]==0:
            v[j]=n
            dfs(n+1, sm+arr[cur][j], j)
            v[j]=0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A, B = map(int, input().split())

    ans = 100*N
    v = [0]*N
    dfs(1, 0, 0)
    print(f'#{test_case} {ans}')