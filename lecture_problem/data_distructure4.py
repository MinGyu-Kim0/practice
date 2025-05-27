# 문자와 숫자가 섞인 문자열에서 숫자만 추출하여 지정된 규칙에 따라 변환 후 합이 0이 되는 연속된 부분 수열을 모두 찾아 출력

# 사용자로부터 알파벳과 숫자가 섞인 문자열을 입력받는다.
input_value = input("입력 문자열: ")

# 문자열에서 숫자만 추출하여 리스트에 저장한다.
lst = []
ch_lst = []
for num in input_value:
    if num.isdigit():
        lst.append(int(num))

# 숫자 리스트에 짝수는 +1 홀수는 -1로 변환해 적용
for change in lst:
    if change % 2 == 0:
        change = 1
        ch_lst.append(change)
    elif change % 2 != 0:
        change = -1
        ch_lst.append(change)
print(f"숫자 추출:{lst}")
print(f"변환된 리스트 (+1/-1): {ch_lst}")

# 변환된 숫자 리스트에서 합이 0이 되는 연속된 부분 수열을 찾아서 출력
print("합이 0인 연속 부분 수열 목록: ")
    
