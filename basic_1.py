# 가위 바위 보 게임 만들기
## - while 과 if 문 활용
import random

winner_count = 0
game = 0
player = 0
computer = 0

gbb = ['가위', '바위', '보']
print("가위바위보 게임을 시작합니다. \n 5판 3선승제입니다")

while winner_count < 5 and player != 3 and computer != 3:

    com = random.choice(gbb)
    me = input("당신의 선택은?")

    if com == me:
        print("비겼습니다.")

    elif (com == '가위' and me == '바위') or (com == '바위' and me == '보') or (com == '보' and me == '가위'):
        print("당신이 이겼습니다.")
        player += 1

    else:
        print("내가 이겼네요.")
        computer += 1
        winner_count = player + computer

    game += 1

    print("게임수 :", game, "플레이어 : ", player, "컴퓨터 : ", computer)

print("게임이 종료되었습니다.")