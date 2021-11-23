# 2 3의 배수의 합 1~1000까지 수중
i = 1
result = 0
while i <= 1000:
    if (i % 3 == 0):
        result += i
    i += 1

print(result)

# 3
n = 10
i = 1
while i <= n:  # 조건문 코드를 완성하자
    print('*'*i)  # 문자열 * 숫자 : 숫자만큼 반복
    i += 1
