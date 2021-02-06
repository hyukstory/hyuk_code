# =============================================================================
# 정규식을 활용한 bs4 고급스킬
# =============================================================================

from bs4 import BeautifulSoup
import re


html = """<html> <head><title>test site</title></head> <body> \
    <div><p id="i" class="a">test1</p><p class="d">test2</p></div> \
        <p class="d">test3</p></p> <a href="/example/test1">a tag</a> \
            <b>b tag</b></body></html>"""


soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())




print(soup.find_all(class_=re.compile('d')))    # 해당 문자열이 포함된 요소를 찾는다
print(soup.find_all(id=re.compile('i')))
print(soup.find_all(re.compile('t')))           # 태그에 t가 포함된 요소 찾기
print(soup.find_all(re.compile('^t')))          # 태그 이름이 t로 시작한느 요소 찾기
print(soup.find_all(href=re.compile('/')))      # href에 슬래시(/)가 포함된 요소 찾기





# 정규식

import re

test_str= "test t1sd j test1"

pattern = re.compile('test')
a = pattern.match(test_str)
b = pattern.search(test_str)
c = pattern.findall(test_str)
d = pattern.finditer(test_str)

print('-- match result --')
print(a)
print(a.group(), a.start(), a.end(), a.span())

print('-- search result --')
print(b)
print(b.group(), b.start(), b.end(), b.span())

print('-- findall result --')
print(c)

print('-- finditer result --')
print(d)
for i in d:
    print(i.group(), i.start(), i.end(), i.span())





import re

test_str= """I am Park Jeong-tae. I live in Paju.
I lived in Paju for 25 years.
Sample text for testing:
abcdefghijklmnopqrsAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42"""

pattern = re.compile('[0-9]')    # 숫자 한자리씩
pattern1 = re.compile('[0-9]+')  # 숫자 덩어리씩
c = pattern.findall(test_str)
d = pattern1.findall(test_str)

print(c)
print(d)





import re

test_str= """I am Park Jeong-tae. I live in Paju.
I lived in Paju for 25 years.
Sample text for testing:
abcdefghijklmnopqrsAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>"'
12345 -98.7 3.141 .6180 9,000 +42 가나다라마바사 이혁수 얍얍 test testssstt"""

pattern = re.compile('[a-z]')
pattern1 = re.compile('[a-z]+')  # a부터 z까지 하나라도 포함
c = pattern.findall(test_str)
d = pattern1.findall(test_str)

print(c)
print(d)

pattern = re.compile('[A-Z]')
pattern1 = re.compile('[A-Z]+')
c = pattern.findall(test_str)
d = pattern1.findall(test_str)

print(c)
print(d)


pattern = re.compile('[A-z]')   # 영어 대무자나 소문자 모두
pattern1 = re.compile('[A-z]+')
e = pattern.findall(test_str)
f = pattern1.findall(test_str)

print(e)
print(f)


pattern = re.compile('[a-zA-Z0-9]+') # a부터 z까지, A부터 Z까지, 0부터 9까지 포함된 것
pattern1 = re.compile('\w+')         # 문자가 하나라도 있으면
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
print(c)
print(d)

pattern = re.compile('[^a-z]+')  # a부터 z까지 포함되지 않는 것
c = pattern.findall(test_str)
print(c)

pattern = re.compile('[^A-Z]+')  # A부터 Z까지 포함되지 않는 것
c = pattern.findall(test_str)
print(c)

pattern = re.compile('t..t')  # t문자문자t 패턴
pattern1 = re.compile('t...t')  # t문자문자문자t 패턴
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
print(c)
print(d)

pattern = re.compile('t?est\w+')  # test나 est로 시작하는 문자열 뒤에 \w가 있어야 됨
pattern1 = re.compile('t?est\w*')  # test나 est로 시작하는 문자열 뒤에 \w가 없어도 됨
c = pattern.findall(test_str)
d = pattern1.findall(test_str)
print(c)
print(d)



# 전화번호 추출
test_num = "저의 전화번호는 010-6666-7777 입니다"

pattern = re.compile('[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')  #숫자숫자숫자-숫자숫자숫자숫자-숫자숫자숫자숫자 형태
pattern1 = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')  #숫자숫자숫자-숫자숫자숫자숫자-숫자숫자숫자숫자 형태
pattern2 = re.compile('\d{3}-\d{4}-\d{4}')  #숫자숫자숫자-숫자숫자숫자숫자-숫자숫자숫자숫자 형태
c = pattern.findall(test_num)
d = pattern1.findall(test_num)
e = pattern2.findall(test_num)
print(c)
print(d)
print(e)
