from pprint import pprint

import requests
from bs4 import BeautifulSoup

# 크롤링 하려는 웹사이트의 소스코드를 읽어온다
response = requests.get("https://www.naver.com/")
assert response.status_code is 200

# selector 객체를 생성
# pprint(response.content)
dom = BeautifulSoup(response.content, "html.parser")
# print(dom)

##p_main_china_1 > div > a > div.main_topic_content
title_lis = dom.select("div.main_topic_content")
print(title_lis)

# titles_lis = dom.find_all("strong", class_="main_topic_title")
# for title in titles_lis:
#     print(title)

# header = dom.select("div#header")
# print(header)