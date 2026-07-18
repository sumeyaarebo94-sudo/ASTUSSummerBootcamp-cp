t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a2 = sorted(a)

    mx1 = a2[-1]
    mx2 = a2[-2]

    for x in a:
        if x == mx1:
            print(x - mx2, end=" ")
        else:
            print(x - mx1, end=" ")
    print()