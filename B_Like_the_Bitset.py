t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    cnt = 0
    ok = True

    for c in s:
        if c == '1':
            cnt += 1
            if cnt >= k:
                ok = False
                break
        else:
            cnt = 0

    if not ok:
        print("NO")
        continue

    print("YES")

    ans = [0] * n
    cur = n

    for i in range(n):
        if s[i] == '0':
            ans[i] = cur
            cur -= 1

    for i in range(n):
        if s[i] == '1':
            ans[i] = cur
            cur -= 1

    print(*ans)