# 구글 이미지 크롤링 라이브러리
# https://pypi.org/project/google_images_download/

# 라이브러리 설치
# pip install google_images_download (X)
# 만일 설치 했다면 살제 할것 : pip uninstall google_images_download
# 기존 사용 불가능 : Unfortunately all 100 could not be downloaded because some images were not downloadable. 0 is all we got for this search filter!

# 다음 수정된 버전으로 다시 설치 할것
# pip install git+https://github.com/Joeclinton1/google-images-download.git
# 참고 : https://tiktikeuro.tistory.com/174
# 키워드당 최대 100개까지 다운로드 가능

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"맑은풍경","limit":100,"print_urls":True, "format":"jpg", "chromedriver":"/usr/local/bin/chromedriver"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
