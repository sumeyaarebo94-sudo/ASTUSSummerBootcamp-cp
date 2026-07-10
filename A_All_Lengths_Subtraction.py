t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    pos = [0] * (n + 1)

    for i in range(n):
        pos[p[i]] = i

    l = min(pos[n], pos[n - 1])
    r = max(pos[n], pos[n - 1])

    ok = (r - l == 1)

    for x in range(n - 2, 0, -1):
        if not ok:
            break

        if pos[x] == l - 1:
            l -= 1
        elif pos[x] == r + 1:
            r += 1
        else:
            ok = False

    print("YES" if ok else "NO")