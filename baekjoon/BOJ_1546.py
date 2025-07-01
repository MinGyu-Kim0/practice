n = int(input())

subjects = list(map(int, input().split()))

max_score = subjects[0]
for max in subjects:
    if max > max_score:
        max_score = max

total = 0
for val in subjects:
    sejun_score = (val/max_score) * 100
    total += sejun_score
    
result = total / n

print(result)
    
    

