import requests
from bs4 import BeautifulSoup
# 안티크롤링 때문에 마치 웹브라우저로 요청하는것 처럼 headers 써주기
response = requests.get("https://news.naver.com/", headers={"User-Agent":"Mozila/5.0"})
assert response.status_code == 200

# print("접속성공")
dom = BeautifulSoup(response.content, "lxml")

main_content = dom.select_one("#main_content")
# select_one()의 결과형 : <class 'bs4.element.Tag'> 요소
# print(type(main_content))

main_components = main_content.select("div.main_component")
# select()의 결과형 : <class 'bs4.element.ResultSet'> 리스트 셋
# print(type(main_components))
# print(main_components[0].text) # 네이버 뉴스들의 title 만 가져온것.

with open("naver_news_headline.text", "w", encoding="utf-8") as fp :
    for main_component in main_components :
        sec_title = main_component.select("div.com_header h4")
        if len(sec_title) != 0 :
            tit = sec_title[0].text
            print(tit)
            fp.write(tit + "\n")

        article_lists = main_component.select("ul")
        for list in article_lists:
            lis = list.select("li div:nth-child(1) a, li a strong")
            for i, a in enumerate(lis):
                sub_tit = f"\t {i} {(a.text).lstrip().rstrip()}"
                print(sub_tit)
                fp.write(sub_tit + "\n")