# x = y = z = 0
# x, y, z = 10, 20, 30 #한 번에 여러 개의 변수값 할당

# x = 100
# y = 200
# print (x,y)

# x, y = y, x
# print(x, y)

# 내가 짠 코드
# price = int(input("물건값을 입력하시오."))
# count1000 = int(input("1000원의 개수를 입력하시오."))
# count500 = int(input("500원의 개수를 입력하시오."))
# count100 = int(input("100원의 개수를 압력하시오."))

# remainPrice = ((count1000 * 1000) + (count500 * 500) + (count100 * 100)) - price

# countRemain500 = int(remainPrice / 500)
# remain = remainPrice % 500
# countRemain100 = int(remain / 100)
# remain2 = remain % 100
# countRemain10 = int(remain2 / 10)
# remain3 = remain2 % 10
# countRemain1 = int(remain3 / 1)

# print(countRemain500, countRemain100, countRemain10, countRemain1)

# 챗지피티가 수정해준 코드
# item_price = int(input("물건값을 입력하세요: "))
# num_1000 = int(input("1000원 지폐 개수를 입력하세요: "))
# num_500 = int(input("500원 동전 개수를 입력하세요: "))
# num_100 = int(input("100원 동전 개수를 입력하세요: "))

# # 총 지불 금액 계산
# total_paid = (num_1000 * 1000) + (num_500 * 500) + (num_100 * 100)

# # 거스름돈 계산
# change = total_paid - item_price

# # 거스름돈 분배
# change_500 = change // 500
# change %= 500

# change_100 = change // 100
# change %= 100

# change_10 = change // 10
# change %= 10

# change_1 = change

# # 결과 출력
# print(f"거스름돈: 500원 {change_500}개, 100원 {change_100}개, 10원 {change_10}개, 1원 {change_1}개")

# age = int(input("나이를 입력하시오."))
# city = input("거주 지역을 입력하시오.")
# print(age >= 20 and city == "인천")

# number = int(input("정수를 입력하시오."))
# if number % 2 == 0 : print("정수입니다.")
# print("끝!")

# number = int(input("나이를 입력하시오."))
# if number < 15 : print("15세가 안 되었군요. 입장이 불가합니다.")
# print("끝!")

# price = int(input("상품의 가격을 입력하시오."))

# if price >= 20000 : shipping_cost = 0
# else : shipping_cost = 3000

# print(f"배송비는 {shipping_cost}원입니다.")

# kor = int(input("국어 점수를 입력하시오."))
# eng = int(input("영어 점수를 입력하시오."))
# math = int(input("수학 점수를 입력하시오."))

# averge = (kor + eng + math) / 3

# if averge > 60 : print("축하합니다!")
# else : print("재시험입니다!")

# id = input("아이디를 입력하시오.")

# if id == "python" : print("환영합니다.")
# else : print("다시 입력해 주세요.")

import random

# x = random.randint(1, 100)
# y = random.randint(1, 100)

# answer = int(input(f"{x} + {y} = "))
# print(x, '+', y, '=', end='')
# answer = int(input())

# if answer == (x+y) : print("정답")
# else : print("오답")

# score = float(input("학점을 입력하시오."))
# eng = int(input("토익 점수를 입력하시오."))

# if score >= 4.0 and eng >= 800 : print("장학금을 받을 수 있습니다.")
# else : print("장학금을 받을 수 없습니다.")

day = int(input("오늘 날짜를 입력하시오."))
car_number = int(input("차량 번호를 입력하시오."))

if day % 2 == 0 : print("오늘은 짝수 차량 입장 가능")
else : print("오늘은 홀수 차량 입장 가능")

if day % 2 == 0 and car_number % 2 : print("귀하의 차량은 오늘 입차 가능합니다.")
elif day % 2 != 0 and car_number % 2 != 0 : print("귀하의 차량은 오늘 입차 가능합니다.")
else : print("귀하의 차량은 오늘 입차 불가합니다.")

score = int(input("점수를 입력하시오."))

if score >= 90 : print("A입니다.")
elif score >= 80 : print("B입니다.")
elif score >= 70 : print("C입니다.")
elif score >= 60 : print("D입니다.")
else : print("F입니다.")