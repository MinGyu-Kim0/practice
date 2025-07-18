# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 
# 그리고 이것은 현재 상근이가 설정한 알람 시간 H시 M분을 의미한다.

# 입력 시간은 24시간 표현을 사용한다. 
# 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다.
# 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.
# 첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)

# 원래 설정할 시간을 입력받는다.
time_h, time_m = map(int, input().split())

# 15(60 - 45)를 더 했을때 60이하라면 시간을 1 낮춘다.
if time_m <= 44:
    time_m = time_m + 15
    if time_h == 0:
        time_h = 24
    time_h = time_h - 1
# 15를 더했을때 60이상인 경우엔 더하지 않고 45를 뺀다.
elif time_m >= 45:
    time_m = time_m - 45
    
# 결과 값 출력
print(time_h, time_m)