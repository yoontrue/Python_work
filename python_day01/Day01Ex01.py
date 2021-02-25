# 사용자 정의 함수 start_run() 선언
# 함수 선언은 def 키워드를 이용한다.
def start_run() :
    # 블럭은 콜론(:) + 탭키를 이용
    # pass
    print('안녕 파이썬 세계!')
    print('Hello Python World1')

# 만약 이 파일을 직접 실행 할 때는 start_run() 실행하고
# 그렇지 않고 다른 파일의 모듈로 들어갈 때는 실행하지 않는다.

if __name__ == '__main__':
    # 사용자 정의 함수 start_run() 호출
    start_run()