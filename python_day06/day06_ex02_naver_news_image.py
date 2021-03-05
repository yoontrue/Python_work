import requests
from bs4 import BeautifulSoup

def getSearchList(juso, selector):
    response = requests.get(juso, headers={"User-Agent":"Mozila/5.0"})
    assert response.status_code == 200

    dom = BeautifulSoup(response.content, "lxml")
    return dom.select(selector)

img_0 = getSearchList("https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=008&aid=0004551950","span.end_photo_org img")[0]
print(img_0.get('src'))