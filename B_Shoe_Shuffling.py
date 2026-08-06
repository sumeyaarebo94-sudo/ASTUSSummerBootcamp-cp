t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    ans = [0] * n
    ok = True

    i = 0
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1

        if j - i == 1:
            ok = False
            break

        for k in range(i, j - 1):
            ans[k] = k + 2
        ans[j - 1] = i + 1

        i = j

    if not ok:
        print(-1)
    else:
        print(*ans)