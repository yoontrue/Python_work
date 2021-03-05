import requests
from bs4 import BeautifulSoup

def getSearchList(juso, selector) :
    response = requests.get(  juso   , headers={"User-Agent":"Mozila/5.0"})
    assert response.status_code == 200

    dom = BeautifulSoup(response.content, "lxml")

    return dom.select(   selector   )



# 실행 결과 테스트
if __name__ == '__main__':
    juso = "https://www.hanbit.co.kr/"
    selector = "div.view_box"
    select_list = getSearchList(juso, selector)

    print(select_list)