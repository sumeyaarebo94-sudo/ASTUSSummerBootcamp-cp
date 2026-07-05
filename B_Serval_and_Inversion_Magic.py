t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    started = False
    ended = False
    ok = True

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if ended:
                ok = False
                break
            started = True
        else:
            if started:
                ended = True

    if ok:
        print("Yes")
    else:
        print("No")