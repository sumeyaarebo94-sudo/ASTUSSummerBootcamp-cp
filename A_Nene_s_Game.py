t = int(input())

for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    ans = []

    for n in queries:
        players = n

        while players >= a[0]:
            removed = 0
            for x in a:
                if x <= players:
                    removed += 1
            players -= removed

        ans.append(players)

    print(*ans)