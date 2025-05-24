# 사용자로부터 난수 생성 개수와 범위를 입력받아 리스트에 난수를 저장하고
# 가장 자주 등장한 숫자 3개를 출력하는 프로그램을 작성하시오.
import random

# 사용자로부터 생성할 난수의 개수, 발생 시작 값 A, 발생 끝 값 B를 입력받는다.
random_num = int(input("난수 개수를 입력하세요: "))
random_start = int(input("시작 범위를 입력하세요: "))
random_end = int(input("끝 범위를 입력하세요: "))

# A ~ B 범위의 난수를 N개 생성하여 리스트에 저장한다.
random_lst = []
for i in range(random_num):
    a = random.randint(random_start, random_end)
    random_lst.append(a)

# 고유 숫자 리스트(중복 x) 생성
own_lst = []
for j in range(len(random_lst)):
    if random_lst[j] not in own_lst:
        own_lst.append(random_lst[j])
print(f"고유 숫자 리스트: {own_lst}")

# 빈도 수 리스트 생성
frequency_lst = []
for n in range(len(own_lst)):
    count = 0
    for m in range(len(random_lst)):
        if own_lst[n] == random_lst[m]:
            count += 1
    frequency_lst.append(count)
print(f"빈도 수 리스트: {frequency_lst}\n")

# 리스트에서 가장 빈도수가 높은 숫자 3개를 찾아 출력.(동점으로 인해 3개가 넘는 경우 모두 출력)
# 미완성
print(f"가장 많이 등장한 숫자 Top3 (동점 포함):")
top3_idx = []
top3_num = []
for idx, num in enumerate(frequency_lst):
    top3_idx.append(idx)
    top3_num.append(num)
# print(top3_idx, top3_num)

# 출력은 숫자와 발생 횟수와 함께 출력

