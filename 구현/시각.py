# 00시 00분 00초 ~ N시 59분 59초 
# 3이 하나라도 포함되는 경우 

h = int(input())

count = 0

for i in range(h+1): # h+1이면 0, 1, ... h 까지
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): # 문자열 자료형으로 변환하여 합치고 '3' 포함되었는지 확인 ex) 03시 20분 35초 -> '032035'에서 '3'이 있는지 확인
                count += 1
