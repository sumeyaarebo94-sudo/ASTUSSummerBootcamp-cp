t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    left = 0
    right = n - 1

    blue_sum = a[left]
    red_sum = a[right]

    blue_count = 1
    red_count = 1

    while left < right:

        if red_sum > blue_sum and red_count < blue_count:
            break

        if red_count >= blue_count:
            left += 1
            blue_sum += a[left]
            blue_count += 1
        else:
            right -= 1
            red_sum += a[right]
            red_count += 1

    if red_sum > blue_sum and red_count < blue_count:
        print("YES")
    else:
        print("NO")