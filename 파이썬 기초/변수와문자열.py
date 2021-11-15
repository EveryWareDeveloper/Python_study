# # # 여러개의 변수를 동시를 초기화
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

# # # 예제 2~5풀기
# # 예제 2

# x = 10
# print(x)

# # 예제 3
# x, y, z = 1, 2, 3

# print(x)
# print(y)
# print(z)

# # 예제 4
# x = 1
# y = 1.1
# z = "문자열"

# print(type(x))
# print(type(y))
# print(type(z))

# # 예제 5
# a = input("a:"+'')
# b = input("b:"+'')

# print("a:"+(b))
# print("b:"+(a))


# 문자열
# 긴 문자열은 따옴표 3개 (''',"""")
var3 = '''
'따옴표 '3 개는 
끝나는 문장까지 
모두를 문자열로 처리
----------------------!
'''
print(var3)

# 문자열 (+) 연산
성 = '홍'
이름 = '길동'
name = 성 + ' ' + 이름
print(name)

# 타입 변환 : str(), int(), float()

print(type(int(str(100))))


# 1
str1 = '\tIt\'s "kind of" sunny\n Have a nice Day!'
print(str1)

# 2
str2 = '''
다스베이더가 말했다. "내가 니 애비다!" 그말을 들은 루크는 '깜짝'놀랐다.
'''
print(str2)
# 3
print("밴드 이름 만들기 프로그램에 환영합니다.")
city = input('태어난 도시가 어딘가요??\n')
petName = input('애완동물의 이름은?\n')
print('당신의 밴드 이름은' + city + ' ' + petName)
# \n 한줄 띄우기
