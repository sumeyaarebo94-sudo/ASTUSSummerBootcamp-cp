t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ans = 0

    for i in range(n):
        r = s[i:] + s[:i]

        cnt = 1
        for j in range(n - 1):
            if r[j] != r[j + 1]:
                cnt += 1

        ans = max(ans, cnt)

    print(ans)