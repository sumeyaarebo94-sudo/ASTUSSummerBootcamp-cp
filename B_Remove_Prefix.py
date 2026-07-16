t = int(input())
for _ in range (t):
    n = int(input())
    a = list(map(int, input().split()))
    seen = set()
    found = False
    for i in range(n-1,-1,-1):
        if a[i] in seen:
            print(i+1)
            found = True
            break
        else:
            seen.add(a[i])
    if not found:
        print(0)

                
    

    