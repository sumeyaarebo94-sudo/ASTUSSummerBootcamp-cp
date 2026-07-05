t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())

    a = sorted(input())
    b = sorted(input())

    i = j = 0
    cnt_a = cnt_b = 0
    ans = []

    while i < n and j < m:
        if cnt_a == k:
            ans.append(b[j])
            j += 1
            cnt_b += 1
            cnt_a = 0
        elif cnt_b == k:
            ans.append(a[i])
            i += 1
            cnt_a += 1
            cnt_b = 0
        elif a[i] < b[j]:
            ans.append(a[i])
            i += 1
            cnt_a += 1
            cnt_b = 0

        else:
            ans.append(b[j])
            j += 1
            cnt_b += 1
            cnt_a = 0

    print("".join(ans))

