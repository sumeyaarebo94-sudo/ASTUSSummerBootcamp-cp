t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    d = {}

    for ch in s:
        d[ch] = d.get(ch, 0) + 1

    print(n - max(d.values()))