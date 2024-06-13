'''
    1~100 사이의 10개의 랜덤수로 리스트를 생성합니다.
    리스트에 저장된 수 중에서 홀수만 리스트에 저장합니다.
    랜덤 생성된 리스트와 홀수 리스트는 오름차순으로 정렬하여 출력하시오.
    랜덤수 저장 변수 : num1
    홀수 저장 변수 : num2
'''
import random
num1 =[]    # 랜덤 수 10개 저장 리스트
num2 = []   # 홀수 저장 리스트

# 1~100 사이의 10개의 랜덤수를 num1 리스트에 저장

for i in range(10) :
    num1.append(random.randint(1,100))
    if num1[i] % 2 != 0 :
        num2.append(num1[i])

num1.sort()
num2.sort()
print("랜덤수 저장 변수 :",num1)
print("랜덤수 저장 변수 :", num2)
print(f'홀수는 {len(num2)}개 입니다.')