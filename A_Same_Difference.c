t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cnt = 1
    ans = 0
    i = n-2
    while i >= 0 and s[i] == s[i+1]:
        cnt += 1
        i -= 1
    while cnt < n:
        ans += 1
        cnt = cnt * 2
    print(ans)
       