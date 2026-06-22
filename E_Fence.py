n, k = map(int, input().split())
h = list(map(int, input().split()))
current = sum(h[:k])

minimum = current
answer = 1
for i in range(k, n):
    current += h[i] - h[i - k]
    if current < minimum:
        minimum = current
        answer = i - k + 2
print(answer)