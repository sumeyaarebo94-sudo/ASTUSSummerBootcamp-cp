n, m = map(int, input().split())
a = list(map(int, input().split()))

forward = [0] * n
for i in range(1, n):
    forward[i] = forward[i - 1]
    if a[i] < a[i - 1]:
        forward[i] += a[i - 1] - a[i]

backward = [0] * n
for i in range(n - 2, -1, -1):
    backward[i] = backward[i + 1]
    if a[i] < a[i + 1]:
        backward[i] += a[i + 1] - a[i]

for _ in range(m):
    s, t = map(int, input().split())

    if s < t:
        print(forward[t - 1] - forward[s - 1])
    else:
        print(backward[t - 1] - backward[s - 1])