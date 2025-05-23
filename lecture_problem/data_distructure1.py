# 사용자로부터 받은 리스트에서 다양한 슬라이싱 방법으로 부분 리스트를 생성한다
lst = []
# 정수 10개를 입력받아 리스트 data 생성
print("정수 10개를 입력하세요.")
for n in range(10):
    element = int(input(f"{n+1}번째 정수: "))
    lst.append(element)

print(f"[원본 리스트]\n{lst}")

# 처음 5개 원소
print(f"1. 처음 5개 원소:\n{lst[:5]}")

# 뒤에서 3개 원소
print(f"2. 뒤에서 3개 원소:\n{lst[-3:]}")

# 짝수 인덱스 원소
print(f"3. 짝수 인덱스 원소:\n{lst[0::2]}")

# 리스트를 거꾸로 뒤집은 결과
print(f"4. 거꾸로 뒤집은 리스트:\n{lst[::-1]}")
