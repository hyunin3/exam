def check(lst):
    cnt = 0
    for i in range(0, N, 3):
        if lst[i] == lst[i+1] == lst[i+2] or lst[i] + 2 == lst[i+1] + 1 == lst[i+2]:
            cnt += 1
    return cnt == 2
        
def dfs(n, tlst):
    global ans
    if n == N:
        if check(tlst):
            ans = 1
        return    
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, tlst+[lst[j]])
            v[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = 6
    lst = list(map(int, input()))
    v = [0] * N
    ans = 0
    dfs(0, [])
    print(f'#{tc} {ans}')