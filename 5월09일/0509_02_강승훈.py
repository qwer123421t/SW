'''
   작성일 : 2024년 5월 3일
   작성자 : 컴퓨터공학과 202495001 강승훈
   설명 : 사용자로부터 입력받은 무장에서 스페이스바가 몇 개 인지 추력하시오.
          그리고 스페이스바를 없엔 문장을 출력하시오
          
    [알고리즘]
        1. 문장을 입력받는다.
        2. 스페이스가 몇 개인지 출력한다.
        3. 스페이스를 삭제한 문장을 출력한다.
'''
a = input("문장을 입력해주세요 : ")
print("스페이스바의 개수는 : ",a.count(' '))
print('스페이스바를 삭제한 문장은 : ',a.replace(' ',''))