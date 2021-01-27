# < lxml >
# lxml은 html과 body 태그가 포함된 형태로 만들어줌
from bs4 import BeautifulSoup

html1 = """<p>test</p>"""
soup1 = BeautifulSoup(html1, 'lxml')
print(soup1)


html2 = """<html><p>test</p></html>"""
soup2 = BeautifulSoup(html2, 'lxml')
print(soup2)

html2 = """<body><p>test</p></body>"""
soup2 = BeautifulSoup(html2, 'lxml')
print(soup2)

# < html5lib >
# lxml 보다 느림
html3 = """<p>test</p>"""
soup3 = BeautifulSoup(html3, 'html5lib')
print(soup3)


import time
startTime = time.time()
print(startTime)
print('측정하고 싶은 실행 코드')

endTime = time.time() - startTime
print(endTime)


# < lxml VS html5lib >
# 속도 비교
from bs4 import BeautifulSoup

html = """<html><head></head><p>test</p></html>"""

start_time = time.time()
BeautifulSoup(html, 'lxml')
lxml_end_time = time.time() - start_time

start_time = time.time()
BeautifulSoup(html, 'html5lib')
html5lib_end_time = time.time() - start_time

print('lxml 시각측정 : %f' %(lxml_end_time))
print('html5lib 시간측정 : %f' %(html5lib_end_time))
print(html5lib_end_time - lxml_end_time)