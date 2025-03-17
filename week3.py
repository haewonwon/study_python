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
item_price = int(input("물건값을 입력하세요: "))
num_1000 = int(input("1000원 지폐 개수를 입력하세요: "))
num_500 = int(input("500원 동전 개수를 입력하세요: "))
num_100 = int(input("100원 동전 개수를 입력하세요: "))

# 총 지불 금액 계산
total_paid = (num_1000 * 1000) + (num_500 * 500) + (num_100 * 100)

# 거스름돈 계산
change = total_paid - item_price

# 거스름돈 분배
change_500 = change // 500
change %= 500

change_100 = change // 100
change %= 100

change_10 = change // 10
change %= 10

change_1 = change

# 결과 출력
print(f"거스름돈: 500원 {change_500}개, 100원 {change_100}개, 10원 {change_10}개, 1원 {change_1}개")
