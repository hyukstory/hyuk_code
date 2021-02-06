# =============================================================================
#  1. title 출력
#  2. 가격 출력
#  3. url 정보
#  4. dictionary 로 자료 생성
#  5. json type file 로 저장
#               import json
#               file = open("./products.json","w")
#               file.write(json.dumps(products))
#               file.close()
#
# =============================================================================


from bs4 import BeautifulSoup
import requests
import json

file = open("./naver.json", "w")

url = "https://search.shopping.naver.com/search/all?query=%EA%B1%B4%EC%A1%B0%EA%B8%B0&cat_id=&frm=NVSHATC"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
cnt = len(soup.find_all('div', class_='basicList_title__3P9Q7'))

for i in range(0, cnt):
    naver = {}
    metadata = soup.find_all('div', class_='basicList_title__3P9Q7')[i]
    title = metadata.a.get('title')
    print("<제품명> : ", title)  # title

    price = soup.find_all('span', class_='price_num__2WUXn')[i].text
    print("<가격> : ", price)  # 가격

    url = metadata.a.get('href')
    print("<url> : ", url)  # url

    print("===================================================")

    naver = {'제품명': title, '가격': price, 'url': url}
    file.write(json.dumps(naver))

file.close()

