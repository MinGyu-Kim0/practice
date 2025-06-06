# 학생이 30명 있는데 각 학생별로 1번부터 30번까지 출석번호가 붙어있다.
# 교수님이 내준 과제를 28명이 제출했고 제출하지 않은 2명의 출석번호를 구하는 프로그램 작성.
# 총 학생수 30명 리스트 생성
students = [value for value in range(1, 31)]

# 제출한 28명 학생명단 리스트 생성.
submit = []
while True:
    student = int(input())
    if student in submit:
        continue
    else:
        submit.append(student)
    if len(submit) == 28:
        break
# 리스트안에 없는 출석번호 체크
missing = []
for i in students:
    if len(missing) == 2:
        break
    for j in range(28):
        if students[i] in submit:
            break
        else:
            missing.append(students[i])
            break
# 오름차순으로 출석번호 출력
print(missing[0])
print(missing[1])

    