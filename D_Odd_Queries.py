t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]

    total = pref[n]

    for _ in range(q):
        l, r, k = map(int, input().split())

        old_sum = pref[r] - pref[l - 1]
        new_sum = total - old_sum + (r - l + 1) * k

        if new_sum % 2:
            print("YES")
        else:
            print("NO")