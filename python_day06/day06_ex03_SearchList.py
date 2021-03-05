import requests

from SearchList import getSearchList

juso="https://www.hanbit.co.kr"
selector="div.view_box"
dom_list = getSearchList(juso, selector)

for i, view_box in enumerate(dom_list) :
    img_list = view_box.find_all("img", class_="thumb")
    img_juso = juso + img_list[0].get('src')
    img_resp = requests.get(img_juso)
    with open("book_imgs/book_img_"+str(i)+".jpg", "wb") as fp:
        fp.write(img_resp.content)

print("이미지 다운로드 완료!")