t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = 0
    ans = 10**18

    for i in range(n):
        total += a[i]
        ans = min(ans, total // (i + 1))
        print(ans, end=" ")

    print()