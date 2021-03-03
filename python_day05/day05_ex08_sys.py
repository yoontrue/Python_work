# 시스템 모듈

import sys

print(len(sys.argv))

if len(sys.argv) > 1:
   for arg in sys.argv[1:] :
       print(arg)

print(sys.copyright)

# print(sys.getwindowsversion())

print(sys.version)

print(sys.path)

# 프로그램 강제종료
sys.exit()