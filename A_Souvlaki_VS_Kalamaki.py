t = int(input())
for i in range (t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ok = True
    for i in range (n-1):
        if a[i] != a[i+1] and  (i+1) % 2 == 0:
            ok = False
            break
    if ok:
        print("YES")
    else:
         print("NO")
    