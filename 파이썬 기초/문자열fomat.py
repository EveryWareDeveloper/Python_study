# f - string
from types import BuiltinFunctionType


# name = '홍길동'
# age = 20
# print(f'안녕하세요 {name}님 나이가 {age}살 이시군요')

# 2. 문자열   .format()
welcome = '환영합니다.'
number = 20

print('{}번 손님 {}' .format(number, welcome))

# 변수 name과 color에 자신의 이름과 좋아하는 색상을 문자열로
# .format() 방법과 f-string  방법으로 괄호안을 수정해서 자신의  이름과 좋아하는
# 색상을 출력해보세요

name = '강범희'
color = 'Blue'
print('안녕하세요 제이름은{}이고 좋아하는색상은 {}입니다.' .format(name, color))
print(f'안녕하세요 제이름은 {name}이고 좋아하는 색상은 {color}입니다.')

#  문자열 인덱스 : 문자열은 인덱스 번호를 사용가능

string1 = "abcdefg"
print(string1[2], string1[1])  # c

print(string1[1:5])  # bcde
# 슬라이싱 [ 시작인덱스: 끝인덱스-1 ], [ : : 증감]
print(string1[::-1])  # 역순으로

# 인덱스 번호로 값을 가져오는 것은 가능하지만 수정불가

# string1[0] ='k';
print(len("문자열의길이?"))

# 1
# ex1 = input("두 자리 숫자를 입력: \n")
# x = ex1[0]
# y = ex1[1]
# z = int(x) + int(y)

# print(f'{z}')

height = input("키입력 : ")
weight = input("몸무게입력 : ")

BMI = float(weight) / float(height)**2
print(f'당신의 bmi는 {round(BMI,2)}입니다')
