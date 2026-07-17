t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    used = set()
    ans = []
    extra = []

    for x in a:
        if x not in used:
            used.add(x)
            ans.append(x)
        else:
            extra.append(x)

    ans.extend(extra)

    print(*ans)