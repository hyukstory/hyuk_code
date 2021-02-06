# 숫자 up & down 게임 만들기
## - while 과 if 문 활용
import random

rn = random.randrange(1, 101, 1)
user = 0
count = 0

print("1~100 숫자 up % down 게임을 시작합니다.")

while user != rn:

    user = int(input("1 ~ 100 사이의 숫자를 입력하세요 : "))

    if user > rn:
        print("down")

    elif user < rn:
        print("up")

    count += 1

print("정답입니다.")

print(count, "번만에 성공하셨습니다.")
