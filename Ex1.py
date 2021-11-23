# 연습문제
# 01. 두 수의 곱을 리턴하는 함수

def mult_two(a, b):
    # 함수를 완성시킨다.
    return a*b


if __name__ == '__main__':
    print(mult_two(3, 2))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0

# 2.튜플 (3개 입력 이상) 을 입력받아서
# 첫번째 값, 세번째 값, 끝에서 두번째 값을 튜플로 만들어 리턴


def easy_unpack(e):
    return (e[0], e[2], e[-2])  # 튜플로 리턴


if __name__ == '__main__':
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)

# 3. 한 단어만 끊어서 리턴한다.
# 만약 끊어진 단어가 없다면 단어 전체 리턴


def first_word(text):
    return text.split()[0]


if __name__ == '__main__':
    print(first_word("Hello world"))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"


# 04. 패스워드는 길이가 6보다 커야 한다. => 크면 True 틀리면 False 리턴
def is_acceptable_password(password):
    return len(password) > 6


if __name__ == '__main__':
    print(is_acceptable_password('short'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False


# 05. 정수(int)의 길이를 구하라.
def number_length(a):
    return len(str(a))


if __name__ == '__main__':
    print(number_length(10))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert number_length(10) == 2
    assert number_length(0) == 1
    assert number_length(4) == 1
    assert number_length(44) == 2

# 06. 문자열을 입력 받아서 역순으로 리턴


def backward_string(val):
    return val[::-1]


if __name__ == '__main__':
    print(backward_string('val'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'


# 07. 리스트 items 와 정수 i를 입력받아,만약 i가 items에 있으면 i 앞의 숫자들을 제거하고 리턴
def remove_all_before(items, i):
    if i in items:  # i가 리스트에 있을경우
        return items[items.index(i):]
    else:         # i가 리스트에 없을경우
        return items


if __name__ == '__main__':
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [
        7, 7, 7, 7, 7, 7, 7, 7, 7]

# 8 text 문자열을 입력받아 문자열의 문자가


def is_all_upper(text):
    return text.upper() == text


if __name__ == '__main__':
    print(is_all_upper('ALL UPPER'))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True

# 09 리스트를 입력받아 첫번째 아이템을 맨 마지막으로 보낸다음 리턴,


def replace_first(items):
    if len(items) > 1:  # 리스트의 길이가 2이상일때
        items.append(items.pop(0))
    return items  # 빈리스트[] 또는 아이템이 하나 [1] 일때 그냥 리턴


if __name__ == '__main__':
    print(list(replace_first([1, 2, 3, 4])))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []

# 10. 양수를 입력받아서 숫자의 자릿수중에 가장 큰수(0~9)가 리턴


def max_digit(number):
    return int(max(str(number)))


if __name__ == '__main__':
    print("Example:")
    print(max_digit(0))

    # 다음과 같이 리턴결과가 나와야 한다.
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
