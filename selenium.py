
# =================================================
# 크롬드라이버 다운 받아야함
# chrome 열고 -> 설정 -> chrome 정보 -> 버전 확인  (84)
#
# chrome 검색창에 "chrome 드라이버 다운로드' 검색 -> 버전에 맞는 파일 다운
# C 드라이브에 TEMP 파일 생성 후 거기에 압축 해제
# =================================================





from selenium import webdriver
import time

url = 'https://pjt3591oo.github.io/search'

driver = webdriver.Chrome('C:/TEMP/chromedriver.exe')   # 빈 브라우저 띄움
time.sleep(3)
driver.get(url) # url 접속


selected_id = driver.find_element_by_id('nav-trigger')
print(selected_id)
print(selected_id.tag_name)
print(selected_id.text)





selected_tag_p = driver.find_element_by_tag_name('p')
print(selected_tag_p)
print(selected_tag_p.tag_name)
print(selected_tag_p.text)

selected_tags_p = driver.find_elements_by_tag_name('p')
print(selected_tags_p)





selected_name = driver.find_element_by_name('query')
print(selected_name)
print(selected_name.tag_name)
print(selected_name.text)

selected_names = driver.find_elements_by_name('query')
print(selected_names)




url = 'https://pjt3591oo.github.io'

driver = webdriver.Chrome('C:/TEMP/chromedriver.exe')
driver.get(url)

selected_link = driver.find_element_by_link_text('')
print(selected_link)
print(selected_link.tag_name)
print(selected_link.text)

selected_links = driver.find_elements_by_link_text('')
print(selected_links)






# =============================================================================
#         selenium 과 bs4 같이 활용하여 크롤
# =============================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

url = 'https://pjt3591oo.github.io/search'

search_keysword = 'db'

driver = webdriver.Chrome('C:/TEMP/chromedriver.exe')
driver.get(url)


selected_tag_a = driver.find_element_by_css_selector('input#search-box')

selected_tag_a.send_keys(search_keysword)
selected_tag_a.send_keys(Keys.ENTER)  # ‘\ue007’로 해도 엔터가 됨

soup = BeautifulSoup(driver.page_source, 'lxml')
items = soup.select('ul#search-results li')

for item in items:
    title = item.find('h3').text
    description = item.find('p').text
    print(title)
    print(description)

