# engScore = 90
# mathScore = 35
# korScore = 88
# scoreSum = engScore + mathScore + korScore
# scoreAverge = scoreSum / 3
# print("세 과목의 평균은", scoreAverge, "점입니다.")

# pi = 3.14
# radius = 5
# height = 10
# volume = pi * radius**2 * height
# print(volume)

# name = input("이름을 입력하세요.")
# print(name, "씨 안녕하세요!")

# a = input("a를 입력해 주세요.")
# b = input("b를 입력해 주세요.")
# sum = a + b
# print(sum) # error

# a = int(input("a를 입력해 주세요."))
# b = int(input("b를 입력해 주세요."))
# sum = a + b
# print(sum)

# s1 = "100"
# print(int(s1) + 1)

# a = "123.4"
# print(int(a)) # error

# engScore = int(input("영어 점수를 입력해 주세요."))
# mathScore = int(input("수학 점수를 입력해 주세요."))
# korScore = int(input("수학 점수를 입력해 주세요."))
# scoreSum = engScore + mathScore + korScore
# scoreAverge = scoreSum / 3
# print("세 과목의 평균은", scoreAverge, "점입니다.")

# a = int(input("a를 입력해 주세요."))
# b = int(input("b를 입력해 주세요."))
# print(a, "의", b, "승은", a**b, "입니다.")

# name = "홍길동"
# address = "서울"
# print(f"저의 이름은 {name}입니다. 저는 {address}에 삽니다.")

first = int(input("첫 번째 숫자를 입력해 주세요: "))
second = int(input("두 번째 숫자를 입력해 주세요: "))

print("%d + %d = %d" % (first, second, first + second))
print("%d - %d = %d" % (first, second, first - second))
print("%d * %d = %d" % (first, second, first * second))
print("%d / %d = %.2f" % (first, second, first / second))  # 나누기는 소수점까지 표시
