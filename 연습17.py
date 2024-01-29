#연습17.py

from bs4 import BeautifulSoup

page = open('c:\\work\\test01.html', 'rt', encoding='utf-8').read()
soup = BeautifulSoup(page, 'html.parser')
# print(soup.prettify())
#문서 내부에 <p> 태그 전부 검색하기
# print(soup.find_all("p"))

#이번에는 하나의 <p> 태그만 검색
print(soup.find('p'))

#특징이 있는<p class='outer-text> 태그 검색
print(soup.find_all('p', class_="outer-text"))

#특징이 있는 <p class='outer-text> 태그 검색
print(soup.find_all("p", class_='outer-text'))
#atts 속성을 지정해서 검색
print(soup.find_all("p", attrs={'class' : 'outer-text'}))
#태그의 id='first' 인것을 검색
# print(soup.find_all(id='first'))

# # <p>태그를 검색해서 태그 내부에 있는 문자열을 가져온다.
# for tag in soup.find_all('p'):
#     print(tag.text.strip())

#<p> 태그를 검색해서 태그 내부에 있는 문자열을 가져온다.
for tag in soup.find_all('p'):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)

