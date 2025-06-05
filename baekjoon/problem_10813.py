# N개의 바구니 각각 1번부터 N번까지 번호가 매겨져 있음.
# 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 공이 들어있다.
# M번 공을 바꿀때 바구니 2개를 선택하여 두 바구니의 공을 서로 교환한다.
# 공을 어떻게 바꿀지 주어졌을 때, M번 공을 바꾼 이후 각 바구니에 어떤 공이 들어있는지 구하는 프로그램 작성

# 사용자로부터 바구니의 개수와 교환횟수를 입력받는다.
basket, count = map(int, input().split())

# 바구니 목록을 만든다.
baskets = [basket for basket in range(1, basket+1)]

# 교환할 바구니를 입력받고 인덱스 값으로 위치 변환
for _ in range(count):
    N, M = map(int, input().split())
    baskets[N-1], baskets[M-1] = baskets[M-1], baskets[N-1]

# unpacking으로 풀어서 출력
print(*baskets)
    




 
