# 예제 1
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")
##답 : shirt

# 예제 2

i = 1
result = 0
while i <= 1000:
    if(i % 3 == 0):
        result += i
    i += 1
print(result)

# 예제 3

n = 5
i = 1
while i <= n:  # 조건문 코드를 완성하자
    print('*'*i)  # 문자열 * 숫자 : 숫자만큼 반복
    i += 1
