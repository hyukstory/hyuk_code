## 로또 번호 웹크롤링

### 로또 900회

from bs4 import BeautifulSoup
import requests

html = requests.get('https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=900')
# pprint(html.text)

soup = BeautifulSoup(html.text, 'html.parser')
print(soup)

data1 = soup.find('div', {'class': 'win_result'})
data1

i = 0
for i in range(0, 7):
    data2 = data1.findAll('span')[i].text
    print(data2)
    lotto = open("로또 번호.txt", "a")
    lotto.write(data2 + ",")
    lotto.close()

    i = i + 1

### 로또 900회 ~ 923회

from bs4 import BeautifulSoup
import requests

url1 = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
lotto = open("로또 번호2.txt", "a", encoding="UTF-8")

for url2 in range(900, 924):
    url = url1 + str(url2)
    lotto.write(str(url2) + "회 : ")
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    data1 = soup.find('div', {'class': 'win_result'})

    i = 0
    d = []
    for i in range(0, 7):
        data2 = data1.findAll('span')[i].text  # list에 넣어서 결과 보기
        d.append(data2)
        i = i + 1
    lotto.write(str(d))
    lotto.write("\n")

lotto.close()

### API 활용하여 웹크롤링

##### https://somjang.tistory.com/entry/Python%EB%A1%9C%EB%98%90-api%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%98%EC%97%AC-%EC%97%AD%EB%8C%80-%EB%A1%9C%EB%98%90-%EB%8B%B9%EC%B2%A8-%EA%B2%B0%EA%B3%BC-%EB%B6%84%EC%84%9D%ED%95%B4%EB%B3%B4%EA%B8%B0

import pandas as pd
import requests
from tqdm import tqdm
import json


def getLottoWinInfo(minDrwNo, maxDrwNo):
    drwtNo1 = []
    drwtNo2 = []
    drwtNo3 = []
    drwtNo4 = []
    drwtNo5 = []
    drwtNo6 = []
    bnusNo = []
    totSellamnt = []
    drwNoDate = []
    firstAccumamnt = []
    firstPrzwnerCo = []
    firstWinamnt = []

    for i in tqdm(range(minDrwNo, maxDrwNo + 1, 1)):  # tqdm : 시간의 경과에 따라 진행률 보여줌
        req_url = "http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + str(i)
        req_lotto = requests.get(req_url)
        lottoNo = req_lotto.json()
        drwtNo1.append(lottoNo['drwtNo1'])
        drwtNo2.append(lottoNo['drwtNo2'])
        drwtNo3.append(lottoNo['drwtNo3'])
        drwtNo4.append(lottoNo['drwtNo4'])
        drwtNo5.append(lottoNo['drwtNo5'])
        drwtNo6.append(lottoNo['drwtNo6'])
        bnusNo.append(lottoNo['bnusNo'])
        totSellamnt.append(lottoNo['totSellamnt'])
        drwNoDate.append(lottoNo['drwNoDate'])
        firstAccumamnt.append(lottoNo['firstAccumamnt'])
        firstPrzwnerCo.append(lottoNo['firstPrzwnerCo'])
        firstWinamnt.append(lottoNo['firstWinamnt'])
        lotto_dict = {  # "추첨일":drwNoDate,
            "Num1": drwtNo1,
            "Num2": drwtNo2,
            "Num3": drwtNo3,
            "Num4": drwtNo4,
            "Num5": drwtNo5,
            "Num6": drwtNo6,
            "bnsNum": bnusNo
            # "총판매금액":totSellamnt,
            # "총1등당첨금":firstAccumamnt,
            # "1등당첨인원":firstPrzwnerCo,
            # "1등수령액":firstWinamnt
        }

    df_lotto = pd.DataFrame(lotto_dict)
    return df_lotto


#### pd.read_csv("lotto_win_info.csv")

lotto_df = getLottoWinInfo(1, 923)

lotto_df.to_csv("lotto.csv", index=False)

#### 웹크롤링하는 함수 만들기

from bs4 import BeautifulSoup
from pprint import pprint
import requests
from tqdm import tqdm


def 혁수의로또():
    파일이름 = input("파일 이름을 적어주세요 : ")
    시작 = int(input("시작 회차를 적어주세요 :"))
    끝 = int(input("마지막 회차를 적어주세요 :"))

    url1 = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo="
    lotto = open(파일이름 + ".txt", "a", encoding="UTF-8")

    for url2 in tqdm(range(시작, 끝)):
        url = url1 + str(url2)
        lotto.write(str(url2) + "회 : ")
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        data1 = soup.find('div', {'class': 'win_result'})

        i = 0
        d = []
        for i in range(0, 7):
            data2 = data1.findAll('span')[i].text  # list에 넣어서 결과 보기
            d.append(data2)
            i = i + 1
        lotto.write(str(d))
        lotto.write("\n")

    lotto.close()
    return print("인생은 한방!")


혁수의로또()

#### 로또 번호 생성 함수 직접 만들어 보기

import random


def 로또번호랜덤추출():
    # 숫자 외 다른 것을 입력할 시엔 예외 처리!
    try:
        게임수 = int(input("번호를 몇 개 생성할까요(숫자만 입력) : "))
    except ValueError:
        print("숫자만 입력할 수 있습니다.")

    i = 1
    for i in range(1, 게임수 + 1):
        lotto = random.sample(range(1, 46), 6)
        print("[%d]: " % i, lotto)


로또번호랜덤추출()
