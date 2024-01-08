# 카테고리로 구분하기 위해
## 클래스: 객체라는 주어로 묶는 방법
## 모듈: 관심사를 기반으로 묶는 방법
### math 모듈 -> 수학과 관련된 대상
### random 모듈 -> 랜덤 처리 관련 대상
### sys 모듈 -> 시스템 관련 대상

# 1. import 모듈
# "모듈"을 식별자로 읽어들임
import math
print(math.sin(1))
print(math.cos(1))
print(math.tan(0))

# 2. import 모듈 as 모
# 모듈을 "모"라는 식별자로 읽어들임
import math as m
print(m.sin(1))
print(m.cos(1))
print(m.tan(0))

# 3. from 모듈 import 변수, 함수, 클래스
# "변수, 함수, 클래스"를 식별자로 읽어들임
from math import sin, cos, tan
print(sin(1))
print(cos(1))
print(tan(0))