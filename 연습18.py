#연습18.py

#당근마켓 크롤링 하기
#선택한 영역을 주석처리하기 : ctrl + /

# <div class="cards-wrap">
#       <article class="card-top ">
#   <a class="card-link " data-event-label="710707737" href="/articles/710707737">
#     <div class="card-photo ">
#         <img alt="유아용품 재고정리합니다" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/e746a35ce6e00b875262faa8d0d053a25e2bd8508bf9e61d8c1b1bc41a3d213b.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">유아용품 재고정리합니다</h2>
#       <div class="card-price ">
#         1원
#       </div>
#       <div class="card-region-name">
#         충남 아산시 배방읍
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 20
#           </span>
#         ∙
#         <span>
#             채팅 76
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="708853395" href="/articles/708853395">
#     <div class="card-photo ">
#         <img alt="LG그램 중고노트북 판매합니다" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/0ef6bc0c7d0f868333d4ae80fe4e4adce3543c3bb059faf6ec57ada1e0d003e3_0.webp?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">LG그램 중고노트북 판매합니다</h2>
#       <div class="card-price ">
#         30,000원
#       </div>
#       <div class="card-region-name">
#         경기도 화성시 남양읍
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 25
#           </span>
#         ∙
#         <span>
#             채팅 23
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="708789097" href="/articles/708789097">
#     <div class="card-photo ">
#         <img alt="몽클레어 패딩 사이즈100" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/efc1de8bb19bf5810e67175f31340d2cee763f9d1995790ec9ae4cf297a0a366_0.webp?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">몽클레어 패딩 사이즈100</h2>
#       <div class="card-price ">
#         67,000원
#       </div>
#       <div class="card-region-name">
#         부산 해운대구 우동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 35
#           </span>
#         ∙
#         <span>
#             채팅 67
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="710709010" href="/articles/710709010">
#     <div class="card-photo ">
#         <img alt="책 재고정리" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/457894cbf55cb136101c5fb5c9d76771d11eabef936121b10474f1ff77cc434b.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">책 재고정리</h2>
#       <div class="card-price ">
#         3,000원
#       </div>
#       <div class="card-region-name">
#         충남 아산시 탕정면
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 14
#           </span>
#         ∙
#         <span>
#             채팅 56
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="710677112" href="/articles/710677112">
#     <div class="card-photo ">
#         <img alt="다이슨 무선 청소기 판매합니다" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/269d2c46a919dc4cb16de4f4e13e07f525efd2c2f32ed57a369e4c43286a83e6_0.webp?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">다이슨 무선 청소기 판매합니다</h2>
#       <div class="card-price ">
#         10,000원
#       </div>
#       <div class="card-region-name">
#         대전 중구 태평2동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 18
#           </span>
#         ∙
#         <span>
#             채팅 26
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="708404286" href="/articles/708404286">
#     <div class="card-photo ">
#         <img alt="🔥급하게 이사가서🔥" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/baf97bb27013a421e2f239d5f4f7449903d0728388705ea68b971da8e3304cac.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">🔥급하게 이사가서🔥</h2>
#       <div class="card-price ">
#         나눔🧡
#       </div>
#       <div class="card-region-name">
#         전북 전주시 완산구 효자3동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 13
#           </span>
#         ∙
#         <span>
#             채팅 7
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="710334031" href="/articles/710334031">
#     <div class="card-photo ">
#         <img alt="묵은쌀30kg" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/16305b96fdd3a14615d328872f633478eadd0596a50ee14b0f08f7587bbb572d_0.webp?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">묵은쌀30kg</h2>
#       <div class="card-price ">
#         5,000원
#       </div>
#       <div class="card-region-name">
#         경기도 안산시 단원구 초지동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 8
#           </span>
#         ∙
#         <span>
#             채팅 20
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="709807094" href="/articles/709807094">
#     <div class="card-photo ">
#         <img alt="하우스 한라봉 택배가능" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/9450392cb05118fb22b61d72de4d0e24cbffbcdd66fb14b6b9e74e674bfbb016_0.webp?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">하우스 한라봉 택배가능</h2>
#       <div class="card-price ">
#         3,500원
#       </div>
#       <div class="card-region-name">
#         제주 제주시 도남동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 86
#           </span>
#         ∙
#         <span>
#             채팅 70
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="710735153" href="/articles/710735153">
#     <div class="card-photo ">
#         <img alt="나이키 의류 일괄 처분합니다." src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/0e53f6ac5ea3b20b7a77a62b6b67ff0a20cf256aba37d5778f4469e8dddb2e3e.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">나이키 의류 일괄 처분합니다.</h2>
#       <div class="card-price ">
#         10,000원
#       </div>
#       <div class="card-region-name">
#         부산 사하구 하단제1동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 12
#           </span>
#         ∙
#         <span>
#             채팅 23
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="710441832" href="/articles/710441832">
#     <div class="card-photo ">
#         <img alt="추피 생활이야기 전집(60권) + 낱말놀이책(10권)" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/ba6dc80b24392520d95e32d59c6e612819405d3ab63144dc07279aecd693c4dc.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">추피 생활이야기 전집(60권) + 낱말놀이책(10권)</h2>
#       <div class="card-price ">
#         25,000원
#       </div>
#       <div class="card-region-name">
#         부산 부산진구 양정제2동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 10
#           </span>
#         ∙
#         <span>
#             채팅 35
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="710510527" href="/articles/710510527">
#     <div class="card-photo ">
#         <img alt="건조기 세탁기 공기청정기 TV 냉장고 팝니다" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/8bf0a6d022bfac6310c35cb1ad2d63ffc0d9fda27a61eebbbbd509ee17e29daa.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">건조기 세탁기 공기청정기 TV 냉장고 팝니다</h2>
#       <div class="card-price ">
#         250만원
#       </div>
#       <div class="card-region-name">
#         경남 진주시 호탄동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 20
#           </span>
#         ∙
#         <span>
#             채팅 38
#           </span>
#       </div>
#     </div>
# </a></article>
# <article class="card-top ">
#   <a class="card-link " data-event-label="708050647" href="/articles/708050647">
#     <div class="card-photo ">
#         <img alt="아이폰 11 128GB" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/d8db48f4a4ea62113de6d9866f3091debd2f1bfef09bddffc2de74afea630f0e_0.webp?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">아이폰 11 128GB</h2>
#       <div class="card-price ">
#         360,000원
#       </div>
#       <div class="card-region-name">
#         대구 북구 침산2동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 11
#           </span>
#         ∙
#         <span>
#             채팅 42
#           </span>
#       </div>
#     </div>
# </a></article>

#     </div>





import urllib.request
from bs4 import BeautifulSoup

url = "https://www.daangn.com/hot_articles"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')
# <article class="card-top ">
#   <a class="card-link " data-event-label="710510527" href="/articles/710510527">
#     <div class="card-photo ">
#         <img alt="건조기 세탁기 공기청정기 TV 냉장고 팝니다" src="https://dnvefa72aowie.cloudfront.net/origin/article/202401/8bf0a6d022bfac6310c35cb1ad2d63ffc0d9fda27a61eebbbbd509ee17e29daa.jpg?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>
#     <div class="card-desc">
#       <h2 class="card-title">건조기 세탁기 공기청정기 TV 냉장고 팝니다</h2>
#       <div class="card-price ">
#         250만원
#       </div>
posts = soup.find_all ("div" , attrs={"class":"card-top"})
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div", attrs={"class" : "card-price"})
    print("{0}, {1}".format(title.text , price.text))