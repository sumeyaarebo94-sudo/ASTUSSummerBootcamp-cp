t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    for j in range(n - 1):
        if a[j] == 1 and a[j + 1] == 0:
            count += 1

    print(count)