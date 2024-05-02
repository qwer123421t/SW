'''
   작성일 : 2024년 5월 2일
   작성자 : 컴퓨터공학과 202495001 강승훈
   설명 : 정수를 입력받아 정사각형의 넓이를
          계산하여 출력하는 프로그램을 작성하시오
   
   [문제분석]
        정사각형 넓이 = 가로 *세로
        입력 받는 정수는 몇개? 1개
        1개의 정수를 입력 받아 넓이 계산.
        
   [알고리즘]
        1. 한 변의 길이를 입력 받는다.
        2. 넓이를 계산 한다.
        3. 넓이를 출력한다.
'''
length = int(input('정사각형의 한 변의 길이를 입력하시오. : '))
area = length ** 2
print(f'한변의 길이가 {length}인 정사각형의 넓이는 {area}입니다.')
             