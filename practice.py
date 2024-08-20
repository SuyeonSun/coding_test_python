# 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리
from operator import le


a = 5
print(a)
a = 5.0 
print(a)

# 컴퓨터는 실수를 정확히 표현하지 못한다.
a = 0.3 + 0.6
print(a) # 0.899999999999
# round() 함수: 실수형 데이터, 반올림하고자 하는 위치 -1(즉, 해당 자리수까지 나타내라는 뜻)
print(round(123.456, 2)) 

# 수 자료형의 연산
# 나누기
print(7/3) # 파이썬에서 나누기 여산자는 나눠진 결과를 기본적으로 실수형으로 처리 
# 나눈 결과의 몫만을 얻고자 한다면, 몫 연산자를 활용
print(7//3)

# 거듭제곱 연산자
a = 5
b = 3
print(a**b)

# 리스트 자료형
# 비어있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 대괄호 []를 사용한다.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[0])
print(len(a)) # 길이를 구할 때는 len() 함수를 사용
a = list() # 빈 리스트 선언
a = []
# 크기가 n인 1차원 리스트 초기화
n = 10
a = [0] * n # 크기가 n이고 모든 값이 0인 리스트
a[0] = 100
print(a)

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4]) # [2, 3, 4]
print(a[1:]) # [2, 3, 4, 5, 6, 7, 8, 9]

# 리스트 컴프리헨션: 리스트를 초기화 하는 방법
# 2차원 배열은 무조건 리스트 컴프리핸션을 사용해야 한다.
n = 3
m = 4
array = [[0] * m for i in range(n)]
print(array)
array[0][0] = 100
print(array)

# 리스트 관련 메서드
a = [1, 4, 3]
a.append(2)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)
a.insert(1, 100)
print(a)
print(a.count(3)) # 특정 값인 데이터 개수 세기
a.remove(100) # 처음 하나만 제거
print(a)
a.pop(0) # 특정 인덱스 제거
print(a)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
for i in range(len(a)):
    print(a[i])
result = [a[i] for i in range(len(a))]
print(result)
result = [i for i in a if i not in remove_set]
print(result)
result = []
for i in range(len(a)):
    if a[i] not in remove_set:
        result.append(a[i])
print(result)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5}
print( a | b) # 합집합: {1, 2, 3, 4, 5}
print(a - b) # 차집합: {1, 2}
print(b - a) # 차집합: set()
print(a & b) # 교집합: {3, 4, 5}

a = [1, 2, 3]
print(a)
a.extend([4, 5])
print(a)

if (1 > 0 and 1 > -1): print(True)

def add(a, b):
    print(a + b)
add(1, 2)

# 데이터의 개수 입력
n = int(input())
a, b, c = map(int, input().split())
print(a, b, c)
s = input()
print(s)