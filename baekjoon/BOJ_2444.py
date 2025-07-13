# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

n = int(input())

for u in range(n):
    for _ in range(n-1, u, -1):
        print(" ", end="")
    
    for _ in range(u*2+1):
        print("*", end="")
    print()
    

for d in range(n, 1, -1):
    for b in range((n-d)+1):
        print(" ", end="")

    for l in range(d*2-2, 1, -1):
        print("*", end="")
    print()