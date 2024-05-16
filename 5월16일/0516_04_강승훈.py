'''
   작성일 : 2024년 5월 16일
   작성자 : 컴퓨터공학과 202495001 강승훈
   설명 : 로또 번호 만들기
   
   1 ~ 45 사이의 6개 번호
   로또 번호를 생성하고, 오름 차순으로 정렬하시오.
'''
import random

print("로또 번호 생성")
lotto = list()

i = 0 
while True :
    lotto.append(random.randint(1,45))
    i += 1
    if len(lotto) == 6 :
        break
print("이번주 로또 번호 : ",sorted(lotto))


lotto = set() # 빈 세트 생성

print("세트로 생성")
i = 0
while True :
    lotto.add(random.randint(1,45)) # 랜덤 수를 세트에 추가
    i += 1
    if len(lotto) == 6 :
        break
print("이번주 로또 번호 : ",sorted(lotto))