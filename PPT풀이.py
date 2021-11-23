# # 문제 1
# x = int(input("숫자 1: "))
# y = int(input("숫자 2: "))

# print(f"합: {x+y}")

# # 문제 2
# x = int(input("숫자 1: "))
# y = int(input("숫자 2: "))

# print(f"덧셈: {x+y}")
# print(f"뺄셈: {x-y}")
# print(f"곱셈: {x*y}")
# print(f"나눗셈: {x/y:.1f}")

# 문제 4
# import random

# print("숫자 맞추기 게임에 오신 것을 환영합니다.")
# print("6번 안에 숫자를 맞추지 못하면 당신은 죽습니다.")
# print("자, 그럼 시작하겠습니다")

# name = input("이름을 입력하세요: ")
# print(f"{name}님! 1에서 20까지 숫자중 하나를 생각하세요.")
# secretNumber = random.randint(1, 20)

# for count in range(1, 6):
#     guess = int(input("맞춰보세요 \n"))
#     if (secretNumber > guess):
#         print('그 숫자보다 큰수')
#     elif (secretNumber < guess):
#         print('그 숫자보다 작은수')
#     else:
#         break

# if guess == secretNumber:
#     print(f'잘 맞췄어요 {name}님 {count} 번만에 맞췄어요 !')
# else:
#     print(f'틀렸네요. 정답은 {secretNumber} 입니다.')

# # 문제 5번
# def easy_unpack(elements):
#     return (elements[0], elements[2], elements[-2])


# if __name__ == '__main__':
#     print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
#     assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
#     print(easy_unpack((1, 1, 1, 1)))
#     assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
#     print(easy_unpack((6, 3, 7)))
#     assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# 문제 6
# def is_acceptable_password(password):
#     return len(password) > 6

# if __name__ == '__main__':
#     print(is_acceptable_password('short'))
#     assert is_acceptable_password('short') == False
#     print(is_acceptable_password('muchlonger'))
#     assert is_acceptable_password('muchlonger') == True
#     print(is_acceptable_password('ashort'))
#     assert is_acceptable_password('ashort') == False

# 문제 7
# def number_length(a):
#     return len(str(a))


# if __name__ == '__main__':
#     print(number_length(10))
#     assert number_length(10) == 2
#     print(number_length(0))
#     assert number_length(0) == 1
#     print(number_length(4))
#     assert number_length(4) == 1
#     print(number_length(44))
#     assert number_length(44) == 2

# # 문제 8
# def remove_all_before(items, i):
#     if i in items:
#         return items[items.index(i):]
#     else:
#         return items


# if __name__ == '__main__':
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

#     assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]

# 문제 9
def replace_first(items):
    if len(items) > 1:
        items.append(items.pop(0))
    return items


if __name__ == '__main__':
    print(list(replace_first([1, 2, 3, 4])))

    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
