# 파이썬 자료구조
# list, tuple, dictionary, set ...
# 리스트 : 수정 가능한 목록        ex) [1,2,3,4, ...]
# 튜플 : 수정 불가능한 목록        ex) (1,2,3,4, ...)
# 딕셔너리 : 사전 형태의 맵구조     ex) {key1:value, key2:value, key3:value, ...}
# -------- 자바스크립트의 Object, 자바의 Map 구조와 비슷하고 서로 호환된다.
# -------- 파이썬에서 json 모듈을 이용해서 파일 IO 가능
# 셋 : 중복된 데이터 들어가지 않는다. key도 없고 index도 없다.  ex) {1,2,3,4, ...}

# 리스트 구조 사용
# 리스트 선언 및 초기화
# 파이썬에서는 뱀표기법(snake_case) 사용 (가독성이 높다.)
movie_list = ['시네마천국','삼국지','혹성탈출','태권V','기생충','승리호']
print(movie_list)
for i, movie in enumerate(movie_list):
    print(i,movie)

print(f'movie_list[1] : {movie_list[1]}')
print(f'movie_list[1:] {movie_list[1:]}')
print(f'movie_list[:2] {movie_list[:2]}')

# 리스트의 끝에 데이터 추가
movie_list.append('삼진그룹영어토익반')

print(f'append후의 결과 : {movie_list}')

# 리스트 중간에 데이터 삽입
movie_list.insert(2,'해리포터')

print(f'insert후의 결과 : {movie_list}')

# movie_list의 [1]번째 데이터 삭제
del movie_list[1]

print(f'del후의 결과 : {movie_list}')