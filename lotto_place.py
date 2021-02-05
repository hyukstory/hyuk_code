## 로또 명당 찾기

from bs4 import BeautifulSoup
import requests

html = requests.get('https://dhlottery.co.kr/store.do?method=topStore&pageGubun=L645')

soup = BeautifulSoup(html.text, 'html.parser')
soup

data = soup.find('table', {'class': 'tbl_data tbl_data_col'})
data

data2 = data.findAll('td')
data2

data2[3].text  # 3부터 5 간격으로 8개 값들이 소재지

len(data2)  # 테이블 안의 총 셀 개수

# 3부터 시작하는 공차가 5인 등차수열로 len(data2)까지 구하기 ( 5n + 3)

adress = []

i = 0
f = open("명당리스트.txt", "a", encoding="UTF-8")

for i in range(0, len(data2) // 5):
    adress = data2[5 * i + 3].text
    f.write(str(adress) + "\n")

f.close()

## 로또 명당 262회~923회

from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

url1 = "https://dhlottery.co.kr/store.do?method=topStore&pageGubun=L645&drwNo="
f = open("로또 명당 262~923(ver.혁수).txt", "a", encoding="UTF-8")

for url2 in tqdm(range(262, 924)):
    url = url1 + str(url2)
    # f.write("[" + str(url2) + "회] : " + "\n")
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    data = soup.find('table', {'class': 'tbl_data tbl_data_col'})
    data2 = data.findAll('td')

    adress = []
    i = 0

    for i in range(0, len(data2) // 5):
        adress = data2[5 * i + 3].text
        f.write(str(adress) + "\n")

f.close()
