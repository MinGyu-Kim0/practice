t = int(input())


for n in range(t):
    r, s = map(str, input().split())
    r = int(r)
    for m in s:
        print(m*r,end="")
    print()