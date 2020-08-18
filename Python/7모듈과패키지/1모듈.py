
#모듈이란?
# - 파이썬에서는 한번 저의 했던 변수나 함수, 클래스등을 다른 파이썬 프로그램에서도
#   손쉽게 불러와서 사용할수 있도록 하나의 파일로 모아놓는 방법을 제공하며,
#   이것을 모듈이라고 부릅니다.
# - 모듈은 파이썬 프로그램에서 사용할수 있는 여러 정의들과 실행 가능한 구문들을 담고 있는
#    하나의 파이썬 파일 .py파일로써  기본적으로 제공하는 모듈 뿐아니라
#    다른 개발자들이 직접 만든 모듈을 사용하거나
#   자신이 직접 새로운 모듈을 작성하여 사용할수 있다.
#------------------------------------------------------------
#모듈 불러오기 문법
# -파이썬에서는 import문을 사용하여 세가지 방식으로 모듈을 불러올수 있습니다.
# 방법1.  import 모듈명
# 방법2.  from 모듈명 import *
# 방법3.  form 모듈명 import 함수명 또는 클래스명
#설명 : import문은 코드의 어느 위치에서라도 사용할수 있지만, 통상적으로 코드의 맨 앞에 위치하는 것이 가장 좋다
#방법1 과 방법2는 모두 해당 모듈 전체를 불러옵니다.
#방법1은 모듈에 포함된 변수나 함수를 사용할떄마다 매번 모듈명과 함께  닷.연산자를 사용해자 하지만,
#방법2은 변수명이나 함수명만으로도 간편하게 사용할수 있습니다.

#예제 방법1. import 모듈명   <-- 방법으로 math 모듈 사용해보기

#파이썬에서 기본적으로 제공하는 수학관련 모듈인 math모듈을 불러와서 사용
import  math

print(math.pi) #3.141592.....
print(math.pow(2,2)) # 4.0
#만약 모듈명을 함께 사용하지 않으면 파이썬은 해당 변수나 함수가 정의되어 있지 않다고 판단하여
#NameError를 발생 시킬것이다
#print(pi)
#print(pow(2,2))

print("-------------------------------------------------")

#예제 방법2.  from 모듈명 import *   <--- 방법으로 math모듈 사용해보기
from math import *
print(pi)
#결론 : 방법2 를 사용하여 모듈을 임포트 하면 모듈명을 사용하지 않고 변수명이나 함수명만으로 간단하게 사용할수 있다

print("----------------------------------------------------")

#예제  방법3   from 모듈명 import 함수명 또는 클래스명 <---방법으로 math모듈 사용해보기

pi = "내가 정의한 변수 "

from math import pi   #방법3
print(pi)

#결론 : 불러오는 모듈 안에 사용자가 직접 정의한 변수나 함수와 이름이 겹칠 가능성이 언제나 존재 하기떄문에
#이와 같은 상황을 피하기 위해 import문을 언제나 코드의 맨앞에 위치 시키거나
#필요한 변수나 함수만 불러와 사용하는 것이 좋습니다.
#------------------------------------------------------------

#보충!
# - 모듈은 여러 변수와 함수를 가지고 있는 집합체로, 크게 표준모듈과 외부모듈로 나뉩니다.
# - 표준모듈이란? 파이썬에서 기본적으로 내장되어 있는 모듈을 말함
# - 외부모듈이란? 다른 사람들이 만들어서 공개한 모듈을 말함
# - 표준모듈의 종류
#  random모듈
#  sys모듈
#  os모듈
#  datetime모듈
#  time모듈
#  math모듈
#  turtle모듈
#  urllib모듈

#- 외부모듈의 종류
#  requests모듈
#  BeautifulSoup모듈
#  Numpy모듈
#  Matplotlib모듈
#  pandas모듈



















































