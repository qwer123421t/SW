'''
   작성일 : 2024년 4월 4일
   작성자 : 컴퓨터공학과 202495001 강승훈
   설명 : 숫자와 연산자를 입력 받아 사칙연사의 결과 출력
   
    [문제분석]
        필요한 변수 : num1, num2, op
        사칙연산 : + - * /
        두 개의 정수와 연산자를 입력 받는다.
        
        @, #, $ 등은 연산자가 아니다.
        사칙연산을 제외한 나머지 모든 문자는 잘못된 입력이다.
        
    [알고리즘]
        1. 첫번째 숫자를 입력 받는다
        2. 연산자를 입력받는다
        3. 두번째 숫자를 입력받는다
        4. 만약에 연산자가 + 이면
            4.1 덧셈을 계산하여 출력한다
        5. 아니고 연산자가 - 이면
            5.1 뺄셈을 계산하여 출력한다
        6. 아니고 연산자가 * 이면
            6-1. 곱셈을 계산하여 출력한다.
        7. 아니고 연산자가 / 이면
            7-1. 나눗셈을 계산하여 출력한다.
        8. 아니면
            8-1. 해당 연산자는 없습니다. 
'''
#
num1 = int(input("첫번째 수를 입력해 주세요 : "))
op = input("연산자를 입력해주세요. : ")
num2 = int(input("두번째 수를 입력해 주세요 : "))

if op == '+' :
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == '-' :
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == '*' :
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == '/' :
    print(f"{num1} / {num2} = {num1 / num2}")
else :
    print("해당 연산자는 없습니다.")