t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = [0] + list(map(int, input().split()))

    courses = []
    b = list(map(int, input().split()))
    for i in range(n):
        courses.append((b[i], i + 1))

    courses.sort(reverse=True)

    ans = []

    for level, idx in courses:
        while level <= k:
            ans.append(idx)
            level += 1

    print(len(ans))
    print(*ans)