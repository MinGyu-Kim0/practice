# 학생이 30명 있는데 각 학생별로 1번부터 30번까지 출석번호가 붙어있다.
# 교수님이 내준 과제를 28명이 제출했고 제출하지 않은 2명의 출석번호를 구하는 프로그램 작성.
# 총 학생수 30명 리스트 생성
students = [value for value in range(1, 31)]

# 제출한 28명 학생명단 리스트 생성.
submit = []
for _ in range(28):
    submit.append(int(input()))

for i in students:
    if i not in submit:
        print(i)
    