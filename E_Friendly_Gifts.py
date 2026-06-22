import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pos = [[] for _ in range(n + 1)]

    for i in range(n):
        pos[a[i]].append(i)

    dp = [[0] * (n + 2) for _ in range(n + 2)]

    for len_seg in range(1, n + 1):
        for l in range(1, n - len_seg + 2):
            r = l + len_seg - 1

            dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])

            if pos[l] and pos[r]:
                if l == r:
                    dp[l][r] = max(dp[l][r], 1)
                else:
                    first_l = pos[l][0]
                    last_r = pos[r][-1]

                    if first_l < last_r:
                        dp[l][r] = max(
                            dp[l][r],
                            dp[l + 1][r - 1] + 2
                        )

    print(dp[1][n] // 2)