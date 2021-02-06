# =============================================================================
# 네이버 뉴스
# 정치, 경제, 사회, 생활/문화 면 각각 3개씩 뉴스 크롤링
# =============================================================================


from bs4 import BeautifulSoup
import requests


# 본문 url 정보 가져오기 위한 함수 만들기
def contents_url(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    metadata = soup.find_all('div', class_='ranking_headline', limit=3)

    for i in metadata:
        print("http://news.naver.com" + i.a.get('href'))


# 함수 잘되는지 테스트
contents_url("https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=100&date=20200817")

# for 문 활용하여 뉴스기사 크롤링
for i in range(100, 104):
    main_url = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=%s&date=20200817" % (
        i)
    print("[%d 면]" % (i - 99))
    html = requests.get(main_url)
    soup = BeautifulSoup(html.text, 'lxml')
    # metadata = soup.find_all('div', class_ = 'ranking_headline', limit =3)

    for j in range(0, 3):
        title = soup.find_all('div', class_='ranking_headline', limit=3)[j]
        print("<제목> : ", title.text)  # 제목

        views = soup.find_all('div', class_='ranking_view')[j].text
        print('<조회수> : ', views)  # 조회수

        conURL = title.a.get('href')
        conURL_1 = "http://news.naver.com" + conURL
        print("<본문 URL> : ", conURL_1)  # 본문 URL

        html2 = requests.get(conURL_1)
        soup2 = BeautifulSoup(html2.text, 'lxml')
        contents = soup2.find('div', id="articleBodyContents").text
        print("<본문> : ", contents)  # 본문

    print("++++++++++++++++++++++++++++++++++++++")
