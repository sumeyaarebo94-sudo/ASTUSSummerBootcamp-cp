t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    ans = sorted(p)

    for i in range(n - 1):
        if ans[i] == p[i]:
            ans[i], ans[i + 1] = ans[i + 1], ans[i]

    if ans[-1] == p[-1]:
        ans[-1], ans[-2] = ans[-2], ans[-1]

    print(*ans)