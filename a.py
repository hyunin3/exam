T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lstw = list(map(int, input().split()))
    lstt = list(map(int, input().split()))
    lstw.sort(reverse=True)
    lstt.sort(reverse=True)
    i=ans=0
    for n in lstw:
        if n <= lstt[i]:
            ans += N
            i += 1
            if i == M:
                break
    print(f'#{tc} {ans}')        