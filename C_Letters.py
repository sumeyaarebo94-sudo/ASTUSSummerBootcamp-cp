from bisect import bisect_left

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

prefix = []

total = 0
for rooms in a:
    total += rooms
    prefix.append(total)

for letter in b:
    dorm = bisect_left(prefix, letter)

    if dorm == 0:
        room = letter
    else:
        room = letter - prefix[dorm - 1]

    print(dorm + 1, room)