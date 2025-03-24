# import random

# randomNum = random.randint(1, 3)
# myNum = int(input("숫자를 입력하세요."))

# if randomNum == myNum:
#     print("수비에 성공했습니다.")
# else:
#     print("페널티킥에 성공했습니다.")

# yearInput = int(input("연도를 입력하시오."))

# if yearInput % 4 == 0 and yearInput % 100 != 0 or yearInput % 400 == 0:
#     print(f"{yearInput}년은 윤년입니다.")
# else:
#     print(f"{yearInput}년은 윤년이 아닙니다.")

# for i in range(5):
#     print("안녕하세요!")

# aa = [10, 20, 30, 40, 50]
# print(aa[0], aa[1])

# fruit = ["딸기", "사과", "수박", "메론"]

# if "딸기" in fruit:
#     print("딸기가 있네요!")

# else:
#     print("딸기가 없네요...")

# sum = 0

# for i in range(1, 11, 1):
#     sum += i

# print(f"1부터 10까지의 합은 {sum}이다.")

# start = int(input("시작값을 입력해 주세요."))
# end = int(input("종료값을 입력해 주세요."))
# if start > end:
#     end = int(input("종료값을 다시 입력해 주세요."))
#     plus = int(input("증가값을 입력해 주세요."))
# else:
#     plus = int(input("증가값을 입력해 주세요."))

# for i in range(start, end, plus):
#     sum = sum + plus
#     print(sum)

# print(f"{start}에서 {end}까지 {plus}씩 증가한 값의 합: {sum}")

# result = 1

# for i in range(1, 11):
#     result *= i

# print(f"10!은 {result}이다.")

# for i in range(1, 10):
#     result = 9 * i
#     print(f"9 * {i} = {result}")

# num = int(input("몇 단을 진행하시겠습니까?"))

# for i in range(1, 10):
#     result = num * i
#     print(f"{num} * {i} = {result}")

# for i in range(5):
#     for j in range(10):
#         print("*", end="")

#     print("")

# for i in range(1, 8):
#     print("*" * i)

# adj = ["small", "medium", "large"]
# nouns = ["apple", "banana", "grape"]

# for i in adj:
#     for j in nouns:
#         print(i, j)

# for i in range(1, 7):
#     for j in range(1, 7):
#         if i + j == 6:
#             print(i, j)

# for j in range(1, 10):
#     for i in range(2, 10):
#         print(f"{i} * {j} = {i*j:2}", end="\t")
#     print()

# count = 1
# sum = 0

while count <= 10:
    sum = sum + count
    count += 1
    print(f"합계는 {sum}이다.")
