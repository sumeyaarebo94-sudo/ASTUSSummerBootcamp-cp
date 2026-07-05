from collections import deque

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    levels = [deque() for _ in range(k + 2)]
    cnt = [0] * (k + 2)

    for i, x in enumerate(b, 1):
        levels[x].append(i)
        if x <= k:
            cnt[x] += 1

    ans = []
    ok = True

    for lv in range(1, k + 1):
        while cnt[lv]:
            moved = False
            for nxt in range(lv + 1, k + 2):
                if nxt <= k and cnt[nxt] == a[nxt - 1]:
                    continue

                idx = levels[lv].pop()
                cnt[lv] -= 1
                levels[nxt].append(idx)
                if nxt <= k:
                    cnt[nxt] += 1
                ans.append(idx)
                moved = True
                break

            if not moved:
                ok = False
                break

        if not ok:
            break

    if not ok or len(ans) > 1000:
        print(-1)
    else:
        print(len(ans))
        if ans:
            print(*ans)
        else:
            print()