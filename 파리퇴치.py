T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for si in range(N - M + 1):
        for sj in range(N - M +  1):
            sum = 0
            for i in range(si, si + M):
                for j in range(sj, sj + M):
                    sum += arr[i][j]
            if ans < sum:
                ans = sum
    print(f'#{tc} {ans}')                        