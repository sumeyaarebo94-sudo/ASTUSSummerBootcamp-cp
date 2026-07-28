t = int(input())

for _ in range(t):
    n = int(input())

    g = [list(map(int, input().split())) for _ in range(n)]

    p = [0] * (2 * n + 1)

    for j in range(n):
        p[j + 2] = g[0][j]

    for i in range(1, n):
        p[n + i + 1] = g[i][n - 1]

    used = [False] * (2 * n + 1)

    for i in range(2, 2 * n + 1):
        used[p[i]] = True

    for x in range(1, 2 * n + 1):
        if not used[x]:
            p[1] = x
            break

    print(*p[1:])