'''
    키와 몸무게를 입력 받아 BMI를 계산하는 프로그램을 함수를 이용하여 작성하시오.
    BMI를 계산하는 함수는 결과 값을 리턴합니다.
    BMI 계산 결과를 가지고 BMI에 따른 비만 정도를 출력하는 함수를 작성하시오.    
    BMI = 몸무게 / (키 * 키)
    키는 m 단위로 입력 받습니다.
    몸무게는 kg 단위로 입력 받습니다.    
    함수명은 하는 일에 맞게 작명하시오.

    출력 결과를 아래를 참고하시오.    
       BMI          구분
    18.5 미만       저체중
    18.5 ~ 22.9     정상
    23 ~ 24.9       과체중
    25 ~ 29.9       경도비만
    30 이상         고도비만
    
    [출력 결과]
        키를 입력하세요(m단위) : 1.77
        몸무게를 입력하세요(kg단위) : 56.3
        당신의 BMI는 17.97로 저체중입니다.
    
        키를 입력하세요(m단위) : 1.65
        몸무게를 입력하세요(kg단위) : 100.3
        당신의 BMI는 36.84로 고도비만입니다.
'''
def BMI_count(tall, weight) :
    BMI = weight / (tall * tall)
    return (BMI)
def BMI_print(BMI) :
    if BMI < 18.5 :
        print(f'당신의 BMI는 {BMI:.2f}이고 저체중 입니다.')
    elif BMI <= 18.5 and BMI >= 22.9 :
        print(f'당신의 BMI는 {BMI:.2f}이고 정상 체중 입니다.')
    elif BMI<= 23 and BMI >= 24.9:
        print(f'당신의 BMI는 {BMI:.2f}이고 과체중 입니다.')
    elif BMI <= 25 and BMI >= 29.9:
        print(f'당신의 BMI는 {BMI:.2f}이고 경도비만 입니다.')
    else :
        print(f'당신의 BMI는 {BMI:.2f}이고 고도비만 입니다.')
tall = float(input('키를 M단위로 입력해주세요 : '))
weight = float(input('몸무개를 kg단위로 입력해주세요 : '))
BMI = BMI_count(tall, weight)
BMI_print(BMI)