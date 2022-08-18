i, hap = 0, 0

for i in range(501, 1001, 2) :
    hap = hap + 1
    
print("500과 1000 사이에 있는 홀수의 합계 : %d" % hap)

for i in range(501, 1001, 2) :
    if hap % 2 == 1:
        hap = hap
    
print("500과 1000 사이에 있는 홀수의 합계 : %d" % hap)  