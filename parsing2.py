# < bs4 >
# request로 가져운 HTML 코드를 파이썬에서 사용할 수 있도록 바꿔줌
from bs4 import BeautifulSoup

html = """<html> <head><title>test  site</title></head> <body><p>test</p> <p>test1</p> <p>test2</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())  # html 구조로 이쁘게 보여주기

html = """<html> <head><title>test  site</title></head> <body><p>test</p> <p>test1</p> <p>test2</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

print(tag_title)  # title 태그 값
print(type(soup), ',', type(tag_title))

## 태그 정보 가져오기

html = """<html> <head><title>test 123123 site</title></head> <body><p>test</p> <p>test1</p> <p>test2</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

print(tag_title.text)  # 해당 태그의 값
print(tag_title.string)  # 해당 태그의 값 (두개는 차이가 있다.)
print(tag_title.name)  # 해당 태그 이름

## 속성 데이터 가져오기

html = """<html> <head><title class="t" id="ti">test site</title></head><body> <p>test</p> <p>test1</p> <p>test2</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

print(tag_title.attrs)  # attr : 해당 태그의 속성
print(tag_title['class'])  # 해당 태그의 속성에 접근할 때 딕셔너리 [키 : 값] 형태처럼 접근
print(tag_title['id'])

## 키 값이 없어서 KeyError 나는 것을 방지하기 위해 get 함수 사용

html = """<html> <head><title class="t" id="ti">test site</title></head><body> <p>test</p> <p>test1</p> <p>test2</p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_title = soup.title

print(tag_title.attrs)
print(tag_title.get('class'))
print(tag_title.get('id'))
print(tag_title.get('class1'))  # 값이 존재하지 않음
print(tag_title.get('class1', 'default_value'))  # 값이 존재하지 않을 때 'default_value'라고 기본 값을 정함

## 태그의 text와 sting 속성 차이

html = """<html> <head><title>test  site</title></head> <body><p><span>test1</span><span>test2</span></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_p = soup.p

print('text : ', tag_p.text, type(tag_p.text))  # text는 하위 태그들 값까지 전부 출력
print('sting : ', tag_p.sting, type(tag_p.string))  # sting은 정확히 태그에 대한 값만 출력

data_string = tag_p.span.string
print(data_string)  # p 태그에 span이 2개 있으므로 span으로 접근하면 첫번 째 span으로 접근

## 자식 태그 접근하기
### contents 속성 사용
html = """<html> <head><title>test  site</title></head> <body><p><span>test1</span><span>test2</span></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_p_children = soup.p.contents

print(tag_p_children)  # contents 속성을 사용하면 리스트 형태로 자식 태그를 가져온다.

### children 속성 사용
html = """<html> <head><title>test  site</title></head> <body><p><span>test1</span><span>test2</span></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')
tag_p_children2 = soup.p.children
print(tag_p_children2)  # <이터레이터 object> 형태로 반환 -> 반복문을 이용해 사용해야 한다

for child in tag_p_children2:
    print(child.text)

## 부모 태그 접근하기
### parent 속성
html = """<html> <head><title>test  site</title></head>  <body><p><span>test1</span><span>test2</span></p>  </body></html>"""
soup = BeautifulSoup(html, 'lxml')

tag_span = soup.span
tag_title = soup.title

span_parent = tag_span.parent
title_parent = tag_title.parent

print(tag_span)
print(span_parent)

print(tag_title)
print(title_parent)

### parents 속성
#### 가장 최상위 부모 태그까지 가져올 수 있다.
span_parents = tag_span.parents
title_parents = tag_title.parents

print(span_parents)
print(title_parents)  # generator 객체 : 이터레이터 객체 처럼 반복문 이용하면 결과 확인 가능

for parent in span_parents:
    print(parent)

for parent in title_parents:
    print(parent)

## 형제 태그 접근하기
### sibling , next_sibling, previous_sibling

from bs4 import BeautifulSoup

html = """<html> <head><title>test  site</title></head> <body><p><a>test1</a><b>test2</b><c>test3</c></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.a.next_sibling)
print(soup.a.previous_sibling)
print(soup.b.next_sibling)
print(soup.b.previous_sibling)
print(soup.c.next_sibling)
print(soup.c.previous_sibling)

## 다음, 이전 요소 접근하기
### 요소 접근하기 - elements
#### 태그 내부에 있는 값, 태그 전부 접근

from bs4 import BeautifulSoup

html = """<html> <head><title>test  site</title></head> <body><p><a>test1</a><b>test2</b><c>test3</c></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

for i in soup.a.next_elements:
    print(i)

## bs4 여러가지 타입들
### type 검사
from bs4 import NavigableString, Tag

html = """<html> <head><title>test  site</title></head> <body><p><a>ttt<span>123</span><span>123</span></a><b>test2</b><c>test3</c></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

for i in soup.p.next_elements:
    print(i, type(i) == NavigableString, type(i) == Tag)

## 원하는 요소 정확히 접근하기
### find_all()

html = """<html> <head><title>test  site</title></head> <body><p><a>test1</a><b>test2</b><c>test3</c></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('title'))
print(soup.find_all('p'))

### id 값으로 가져오기

html = """<html> <head><title>test  site</title></head> <body><p>test1</p><p id = "d">test2</p><p>test3</p></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(id='d'))

### id 존재 유무로 가져오기

html = """<html> <head><title>test  site</title></head> <body><p>test1</p><p id = "d">test2</p><p>test3</p></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all(id=True))  # id가 존재하는 태그를 리스트로 만들어 가져옴
print(soup.body.find_all(id=False))  # id가 존재하지 않는 태그를 리스트로 만들어 가져옴

### class 속성 가져오기

html = """<html> <head><title>test  site</title></head> <body><p>test1</p><p class= "d">test2</p><p class="c">test3</p></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('p', class_='d'))  # 클래스와 겹치므로 언더바(_)를 붙여 중복피함
print(soup.body.find_all('p', 'd'))  # 언더바 안붙여도 되긴함

### test 속성 이용하기

html = """<html> <head><title>test site</title></head> <body> <p>test1</p><p class="d">test2</p><p class="c">test3</p></p> </body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.find_all('p', text="test1"))
print(soup.find_all('p', text="t"))

### find_all() 연속적으로 사용하기
from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p>test1</p><p class="d">test2</p><p class="c">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.prettify())

tag_body = soup.find_all('body')
tag_p = tag_body[0].find_all('p')

print(type(tag_body), tag_body)
print(type(tag_p), tag_p)

## select()
from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <p id="i" class="a">test1</p><p class="d">test2</p><p class="d">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

print(soup.select('p'))
print(soup.select('.d'))
print(soup.select('p.d'))
print(soup.select('#i'))
print(soup.select('p#i'))

## extract()
### 태그를 지우는 역할
html = """<html> <head><title>test site</title></head> <body> <div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

a = soup.body.extract()

print('제거 항목')
print(a)
print('제거완료')
print(soup)

html = """<html> <head><title>test site</title></head> <body> <div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

for tag in soup.select('p'):
    print(tag.extract())

print('제거완료')
print(soup)

from bs4 import BeautifulSoup

html = """<html> <head><title>test site</title></head> <body> <div><p id="i" class="a">test1</p><p class="d">test2</p></div><p class="d">test3</p></p> <a>a tag</a> <b>b tag</b></body></html>"""

soup = BeautifulSoup(html, 'lxml')

for tag in soup.find_all(['p', 'a']):
    print(tag.extract())

print('제거완료')
print(soup)

# ==========================================================


from bs4 import BeautifulSoup
import requests

url = input("주소를 입력하세요 : ")
html = requests.get(url)
# print(html)
# type(html)
# print(html.text)
soup = BeautifulSoup(html.text, 'lxml')
# print(soup)
# type(soup)

f = open("url.txt", "w", encoding="UTF-8")
f.write(str(soup))
f.close()
