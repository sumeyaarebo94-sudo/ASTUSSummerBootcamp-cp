import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    out = []
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        vals = set(arr)
        ans = []
        for _ in range(m):
            c, l, r = input().split()
            l = int(l)
            r = int(r)
            moved = [x for x in vals if l <= x <= r]
            for x in moved:
                vals.remove(x)
            if c == '+':
                for x in moved:
                    vals.add(x + 1)
            else:
                for x in moved:
                    vals.add(x - 1)
            ans.append(str(max(vals)))
        out.append(" ".join(ans))
    print("\n".join(out))
if __name__ == "__main__":
    solve()