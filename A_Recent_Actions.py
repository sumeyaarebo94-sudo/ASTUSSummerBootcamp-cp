t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    recent = []

    for i in range(1, n + 1):
        recent.append(i)

    ans = [-1] * (n + 1)

    for time in range(m):
        post = p[time]

        if post in recent:
            recent.remove(post)
            recent.insert(0, post)
        else:
            last = recent.pop()

            if last <= n and ans[last] == -1:
                ans[last] = time + 1

            recent.insert(0, post)

    print(*ans[1:])