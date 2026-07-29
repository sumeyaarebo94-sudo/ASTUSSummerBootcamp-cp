n, q = map(int, input().split())
prices = list(map(int, input().split()))

prices.sort(reverse=True)

prefix = [0] * (n + 1)

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + prices[i - 1]

for _ in range(q):
    x, y = map(int, input().split())

    left = x - y
    right = x

    print(prefix[right] - prefix[left])