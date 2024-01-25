#web1.py

#웹크롤링 작업
from bs4 import BeautifulSoup as bf

#페이지를 로딩 (메서드나 함수를 연속으로 호출:메서드 체인)
page  = open(r"c:\work\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = bf(page, "html.parser")

#전체문서보기
# print(soup.prettify())

#<p>를 검색
# print(soup.find_all("p"))

#<p>하나만 검색
#print(soup.find("p"))

#<p class='outer-text'> 조건
#print(soup.find_all("p", class_="outer-text"))

#최근 스타일 : attrs 속성
#print(soup.find_all("p", attrs = {"class":"outer-text"}))

#태그 안족에 컨텐츠만 가져오기 : .text
for tag in soup.find_all("p"):
    title = tag.text.strip()
    print(title)
