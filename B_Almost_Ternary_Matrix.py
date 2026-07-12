t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    a = [[0] * m for _ in range(n)]

    flip = 1

    for i in range(0, n, 2):
        cur = flip
        for j in range(0, m, 2):
            if cur:
                a[i][j] = 1
                a[i][j + 1] = 0
                a[i + 1][j] = 0
                a[i + 1][j + 1] = 1
            else:
                a[i][j] = 0
                a[i][j + 1] = 1
                a[i + 1][j] = 1
                a[i + 1][j + 1] = 0
            cur ^= 1
        flip ^= 1

    for row in a:
        print(*row)