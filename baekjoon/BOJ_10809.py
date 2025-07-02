s = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for idx, val in enumerate(alphabet):
    
    for idx2, val2 in enumerate(s):
        if val == val2:
            print(idx2, end=" ")
            break
    else:
        print(-1,end=" ")    
        
            
 