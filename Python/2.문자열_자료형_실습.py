# 문자열은 어떻게 만들고 사용할까?

# 1> 문자열을 만드는 방법 총 4가지
    #1. 큰따옴표 "로 양쪽 둘러 싸기
        # 예 "Hello World"
    #2. 작은 따옴표 '로 양쪽 둘러 싸기
        # 예 'Hello World'
    #3. 큰 따옴표 3개 """를 연속적으로 써서 양쪽 둘러 싸기
        # 예 """Hello"""
    #4. 작은 따옴표 3개 '''를 연속적으로 써서 양쪽 둘러 싸기
        # 예 '''Hello'''


# 2> 문자열 안에 작은 따옴표나 큰 따옴표를 가히로 포함 시키고 싶을 때?
    #1. 문자열에 작은 따옴표 ' 포함 시키기
        # 예 food = "Python's good"      # Phthon's에 작은 따옴표 '를 포함 시키라면
                                         # 큰 따옴표 "로 둘러 싸야한다!

    #2. 문자열에 큰 따옴표 " 포함 시키기
        # 예 say = '"Python" good"'      # 문자열 내부에 큰 따옴표를 기호로 표현 하고 싶을 때
                                         # 문자열 전체의 양쪽을 ? ' 작은 따옴표로 감싼다!

    #3. 작은 따옴표 ' 또는 큰 따옴표 " 를 문자열에 포함시키는 또다른 방법은 백슬래시 \를 사용하면 된다
    # 즉 백슬러시 기호 \를 작은 따옴표 ' 또는 큰 따옴표 " 앞에 삽입 하면
    # 백 슬러시 기호 \ 뒤에 작은 따옴표 '나 큰 따옴표 "는 문자열을 둘러싸는 기호의 의미가 아니라 ' " 문자기호 그 자체를 뜻하게 된다.
        # 예 food = 'has\'s' or "has\"s"

# 3> 여러 줄인 문자열을 변수에 대입하는 방법
    #1. 문자열의 줄을 바꾸는 이스케이프 코드 \n 삽입하기
        #예 multiline = "Life is too short\nYou need python"

    #2. 연속된 작은 따옴표 '''3개 또는 큰 따옴표 """3개 사용하기
        #작은 따옴표 '''3개를 사용한 경우의 예시
multiline = '''
안녕하세요.
반갑습니다.
'''
        #큰 따옴표 """3개를 사용한 경우의 예시
multiline = """
안녕하세요.
반갑습니다.
"""

#------------------------------------------------------------------------------------------------------

# 문자열 연산하기
    #1> 문자열 더해서 연결하기
head = "Pytone"
tail = " is fun! "
print(head + tail)

    #2> 문자열 곱하기
a="Pytone"
print(a * 2) # a 변수에 저장된 문자열을 두 번 반복해서 연결해라! 라는 뜻이다

    #3> 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

    #4> 문자열 길이 구하기
    #문자열 길이 구하기 -> len함수를 사용하면 구할 수 있다.
a="Life is too short"
b = len(a)
print(b)

#------------------------------------------------------------------------------------------------------

# 문자열 인덱싱 (한문자만? 가리켜 얻는다) 과 슬라이싱 (단어를 잘라낸다)


#1> 문자열 인덱싱 ( 한문자만? 가리켜 얻는) 예제
a = "Hello is"
#    01234567  <--- 전체 문자열중 문자의위치를 가리키는 번허로 0인덱스 위치부터 센다
print(a[1]) # 1위치의 문자 e를 얻어 출력
print(a[4]) # 4위치의 문자 o를 얻어 출력


b = "Hello is"
#  -8,-7,-6,-5,-4,-3,-2,-1  <--- 전체 문자열중 문자의위치를 가리키는 번허로 0인덱스 위치부터 센다
print(b[-1]) # -1위치의 문자 s를 얻어 출력
print(b[-2]) # -2위치의 문자 i를 얻어 출력


#2> 문자열 슬라이싱 (단어를 잘라낸다) 예제
# 슬라이싱 기본 문법1
# a[ 시작번호 : 끝번호 ]  -> a변수에 저장된 문자열 문장에서 시작 인덱스 위치번호의 문자부터..
                           #끝 인덱스 위치번호 이전문자의 문자 단어를 잘라내어 뽑아낸다


a = "Hello is"
#    01234567
b = a[0 : 4]
print(b)

c = a[3 : 6]
print(c)

# 슬라이싱 기본 문법2
#a[시작번호 : 생략]  -> a뱐수에 저장된 문자열 중에서.. 입력한 시작번호부터 그 문자열의 끝까지를 잘라내어 뽑아낸다.

a="Hello is"
#  01234567
c = a[1: ]
print(c)

# 슬라이싱 기본 문법3
#a[생략 : 끝번호]  -> a뱐수에 저장된 문자열 중에서.. 시작번호 부터 입력한 문자열 전 까지 잘라내어 뽑아낸다.

a="Hello is"
#  01234567
d = a[ : 2]
print(d)

# 슬라이싱 기본 문법4
#a[생략 : 생략]  -> a뱐수에 저장된 문자열 중에서.. 처음부터 끝까지 잘라내서 뽑아 낸다

a="Hello is"
#  01234567
e = a[ : ]
print(e)

#슬라이싱 기법으로 문자열 나누기 응용 예제
a = "20010331Rainy"
#    01234567889

year = a[0 :4 ] # 처음부터 a[3]까지의 문자열 '2001'을 잘라내어 변수에 저장
# '0331' 잘라내어 변수에 저장
day = a[4:8]
# 'Rainy' 잘라내어 변수에 저장
weather = a[8:]

#----------------------------------------------------------------------------------

# 문자열 포메팅 이란?
# 문자열 안에 어떤 값을 삽입하는 방법

#1> 문자열 포메팅 따라하기
    #1. 숫자 바로 대입
print("i eat %d apples." %3) # %d자리에 숫자3을 대입한 전체 문자열 i eat 3 apples. 출력된다

    #2. 문자열 바로 대입
print("i eat %s apples." %"five") # %s자리에 문자열 "five"를 대입 함

# 결론 : 숫자를 넣기 위해서는 %d를 써야 하고 ,문자열을 넣기 위해서는 %s를 써야 한다.

    #3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." %number)

    #4. 문자열 2개 이상의 값 대입
number = 1
day = "Hello"
print("%s라고 %d번 인사하기" %(day,number))
# 결론 : 2개 이사의 값을 넣으려면 마지막 % 다음 괄호 안에 콤마로 구분하여 각각의 값을 넣어 주면 된다.

#2> 문자열 포멧코드의 종류
# %s 문자열
# %c 문자1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수
# %% (문자 '%' 자체)

#예제
# 정수값을 문자열에 삽입 하려면 %d를 사용하고,
# 실수값을 문자열에 삽입 하려면 %f를 사용해야 한다
# 하지만... %s를 사용하면 이런 것을 생각하지 않아도 된다
# 왜냐하면 %s는 자동으로 %뒤에 있는 값을 문자열로 자동으로 바꿔서 대입 시켜 주기 때문이다.

# i have 3 apples 출력
number = 3
print("i have %d apples" %(number))
# rate is 3.234 출력
float = 3.234
print("rate is %s" %(float))

#예제
# 포메팅 연산자 %d와 %를 같이 쓸 때는 %s를 사용 한다.
# 98%
print("Error is %d%%" %98)

# 3> 포멧 코드와 숫자 함께 사용하기

#1. 정렬과 공백

# 예제
# %10s는 전체 길이가 10개인? 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 (대입되는 값 1개당 1칸차지)
# 그앞의 나머지는 공백으로 남겨 두라는 의미임

print("%10s" %"h1") # 오른쪽 정렬

# 예제
#1. 'h1'을 전체 문자열에 삽입 할 때, 왼쪽 정렬 시키고 나머지는 빈 공백으로 남겨 두기
print("%-10sjane" %"h1") # 왼쪽 정렬

#2. 소수점 표현하기
# 3.42134234 소수점 네번째 자리 까지만 나타내고 싶은 경우~
# .의 의미는 소수점 포인트를 말하고, 그 뒤의 숫자4는 소수점 뒤에 나올 숫자의 개수를 말함
print("%0.4f" %3.42134234)

# 예제
#숫자 3.42134234를 소수점 네번째 자리 까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽 정렬 하기
print("%10.4f" %3.42134234)

#3> format 함수를 사용한 포메팅
# 설명 ㅣ 문자열의 format 함수를 사용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.

#1. 숫자 바로 대입하기
#예제
#"i eat {0} apples"문자열 중에서 {0} 부분을 숫자 3으로 바꾸기
print("i eat {0} apples".format(3))

#2. 문자열 바로 대입하기

print("i eat {0} apples".format("red"))

#3. 숫자값을 저장된 변수이름으로 대입하기
number = 3
print("i eat {0} apples".format(number))

#4. 2개 이상의 값 넣기
#예제
#{0}은 format 함수의 첫번째 입력값인 number 변수에 저장된 값으로 바뀌고
#{1}은 format 함수의 두번쨰 입력값인 day 변수에 저장된 값으로 바뀐다
number = 10
day = "세계"
a = "Hello {0}번 외치고 {1}여행 가자".format(number,day)
print(a)

#5 {0},{1}과 값은 인덱스 항목 대신 더 편리한 {name}형태로 값 넣기
#   {name} 형태를 사용 할 경우 format() 함수에는 반드시 name=value으 값 형태의 입력값이 있어야만 한다.
#예제
print("안녕하세요! {a}! 잘 {b}드립니다".format(a="여러분", b="부탁"))

#6.  왼쪽 정렬
#예제
# :<10 표현식을 사용하면 치환되는 문자열을 왼쪽정렬하고
# 문자열의 총 자릿수를 10으로 맞출수 있다.
print("{0:<10}".format("h1"))

#7. 오른쪽 정렬
#예제
# :>10 표현식을 사용하면 치환되는 문자열을 오른쪽 정렬하고
# 문자열의 총 자릿수를 10으로 맞출수 있다.
print("{0:>10}".format("h1"))

#8. 가운데 정렬
#예제
# :^ 기호를 사용하여 가운데 정렬하여 삽입 할 수 있다.
print("{0:^10}".format("h1"))

#9. 정렬시 공백 문자 대신에 지정한 문자값으로 채워 넣기
#주의할 점은 채워 넣을 문자값은 정렬 문자 < > ^ 바로 앞에 넣어야 합니다
#예제
#가운데 ^로 정렬하고 빈 공간을 = 문자로 채워서 새로운 h1 데이터를 삽입
print("{0:=^10}".format("h1"))

#예제
#가운데 <로 정렬하고 빈 공간을 ! 문자로 채워서 새로운 h1 데이터를 삽입
print("{0:!<10}".format("h1"))

#10. 소수점 표현하기
#예제
#format 함수를 사용해 소수점을 4자리 까지만 표현 하면서 데이터 삽입
v = 3.42134234
print("{0:0.4f}".format(v)) # 3.4213 출력함

#11. { 또는 } 문자 표현하기
# format 함수를 사용해 문자열 포메팅 할 경우
# {}와 같은 중괄호 문자를 포메팅 문자가 아닌 문자 그대로 사용하고 싶은 경우 { { } } 처럼 2개를 연속해서 사용하면 된다#ㅇ
#예제
print("{{and}}".format()) # {and}

#12. f 문자열 포메팅
# 파이썬 3.6버전 부터 f 문자열 포메팅 기능을 사용 할 수 있다.
#예제
#f 문자열 포메팅은 name, age 변수 값을 생성 한 후에 그 값을 참조 할 수 있다.
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

#예제
#format함수 또는 f문자열 포메팅을 사용해 "!!!python!!!"문자열을 출력 해보자
print("{0:!^12}".format("Python"))

print(f'{"python":!^12}')

#4> 문자열 관련 함수

#1. 문자열 관련 함수

#1. 문자 개수 세기
# 문자열 자료형은 자체적으로 함수를 가지고 있다.
#이름 함수를 다른 말로 문자열 내장 함수라 한다.
#이 내장 함수를 사용하려면 문자열 변수 이름 뒤에 .를 붙인 다음 함수이름을 써주면 된다.

#예제
#문자열 중 문자 b의 개수 되돌려 받기
a = "hobby"
print( a.count('b'))

#2. 전체 문자열 중에서 문자 또는 문자열의 시작 인덱스 위치 알려 주기 1
a = "hello world"
b= a.find('h')
print(b)
c = a.find('H')
print(c)

#2.1 전체 문자열 중에서 문자 또는 문자열의 시작인덱스 위치 알려주기 2
#예제
a="Life is too short"

print(a.index('t'))
#만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생 시킴
#print(a.index('A'))     # 오류발생

#3. 문자열 삽입

#예제
#join 함수는 문자열 abcd문자열의 각각의 문자 사이에 ,를 삽입 한다.
print(",".join('abcd'))

#4. 소문자를 대문자로 바꾸기
#예제
#upper함수는 소문자를 대문자로 바꾸어 준다.
#만약 문자열이 이미 대문자라면 아무 변화도 일어나지 않을 것이다.
f = "h1"
g = f.upper()
print(g)

#5. 대문자를 소문자로 바꾸기
#예제
#lower 함수는 대문자를 소문자로 바꾸어 준다.
a = "H1"
b = a.lower()
print(b)

#6. 왼쪽 공백 지우기
# lstrip() 함수
# 문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다
# lstrip에서 l은 left를 의미한다
a = "   hi   "
print(a.lstrip())

#7. 오른쪽 공백 지우기
#rstrip() 함수
#문자열 중 가장 오른쪾에 있는 한칸 이상의 연속된 공백들을 모두 지운다.
a = "    h1     "
print(a.rstrip())

#8. 양쪽공백제거 : strip()

#9. 문자열 바꾸기
# replace (바뀌게 될 문자열,  바꿀 문자열) 함수

#예제
a = "A B C"
print(a.replace("A","B"))

#10. 문자열 나누기
#split 함수는 a.split() 처럼 ()괄호 안에 아무값도 넣어 주지 않으면
#공백(스페이스, 탭, 엔터)를 기준으로 문자열을 나누어 준다
#만약 b.split(":") cjfja ()안에 특정 값이 있을 경우에는 괄호 안의 기호 : 구분자 기호를 이용해
#문자열을 나누어 준다, 이렇게 나눈 값은 배열(리스트)에 나눈 값을 하나식 저장하여 리스트를 되돌려 준다.

#예제
a = "Life is too short"
b = a.split() # 공백을 기준으로 문자열들을 나누어서 각각 [] <-- 리스트에 담아 []리스트를 반환한다.
print(b)

b = "a:b:c:d"
c = b.split(":") # : 기호를 기준으로 문자열을 나눔
                 # 나눈 문자열들은 새로운 [] 리스트 배열 메모리 공간에 각 요소값으로 저장 됩니다.
                 # [] 리스트 자체를 반환 받습니다 ( 인덱스 값을 부여 받습니다 )

print(c)
