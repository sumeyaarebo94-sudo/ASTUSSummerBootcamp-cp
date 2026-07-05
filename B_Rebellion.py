def solve():
    t = int(input()) 
    for _ in range(t):
        n = int(input())  
        arr = list(map(int, input().split()))

    
        firstOne = -1
        
        lastZero = -1

        for i in range(n):
            if arr[i] == 1 and firstOne == -1:
                firstOne = i
            if arr[i] == 0:
                lastZero = i

        
        if firstOne != -1 and lastZero != -1 and firstOne < lastZero:
            print(1)
        else:
            print(0)