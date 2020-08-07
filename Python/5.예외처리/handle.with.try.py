
# try except 구문을 사용하여 예외 처리하기
# 문법

# try :
#       예외가 발생 할 가능성이 있는 코드
# except:
#       예외가 발생했을떄 실행할 코드

# 설명 :
# 예외가 발생 할 가능성이 있는 코드를 모두 try 구문안에 넣고
# 예외가 발생했을때 실행 할 코드를 모두 except 구문 안에 넣으면 된다
# 이렇게 예외처리를 하면 어떤 상황에 예외가 발생하는지 완벽하게 이해하고 있찌 않아도
# 프로그램이 강제로 죽어버리는 상황을 막을 수 있습니다

try :
 #숫자를 입력 받습니다.

 number_input_a = int(input("정수 입력 : ")) # 예외가 발생 할 가능성이 있는 구문

 print("원의 반지름 : " , number_input_a)
 print("원의 둘레 : " , 2 * 3.14 * number_input_a)
 print("원의 넓이 : " , 3.14 * number_input_a * number_input_a)

except :
    print("무언가 잘못되었습니다") # 예외가 발생 했을 때 실행 할 구문

print("그 다음 코드가 정상 출력 된 후 프로그램을 종료 합니다")

# 코드를 실행하고 정수로 변환 할 수 있는 문자열을 입력해 보세요.
# 코드를 실행하면 프로그램이 강제로 종료되는 일 없이 예외처리를 하고 정상적으로 종료 됩니다.