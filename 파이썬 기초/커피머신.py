coffee = 10  # 커피 수량 10개

while True:  # 무한 반복
    print(f"남은 커피의 양은 {coffee}개 입니다.")
    money = int(input("커피 한잔에 300원 입니다. 돈을 넣어 주세요 : "))
    # 입금한 돈이 300원일때 더 클때, 작을 경우 처리 if elif else
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print(f"거스름돈 {money-300}를 주고 커피를 줍니다.")
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")

    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
