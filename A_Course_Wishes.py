from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pos = [deque() for _ in range(k + 2)]
    cnt = [0] * (k + 2)

    for i in range(n):
        pos[b[i]].append(i + 1)
        cnt[b[i]] += 1

    ans = []

    ok = True

    for level in range(k, 0, -1):
        while cnt[level] > a[level - 1]:
            if not pos[level]:
                ok = False
                break

            course = pos[level].popleft()
            ans.append(course)

            cnt[level] -= 1
            cnt[level + 1] += 1
            pos[level + 1].append(course)

        if not ok:
            break

    if not ok:
        print(-1)
    else:
        ans.reverse()
        print(len(ans))
        print(*ans)