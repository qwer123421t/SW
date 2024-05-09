'''
   작성일 : 2024년 5월 3일
   작성자 : 컴퓨터공학과 202495001 강승훈
   설명 : 
'''
# 문자열
name = '강승훈' # 문자열을 변수에 저장

#리스트
city =['서울시', 800, '부산시', 400] # 리스트 생성

#튜플
num = (100, 200, 300, 400) # 튜플 생성

'''
1. 인덱싱(indexing) : 순차적인 자료 구조에 인덱스(첨자) 값을 가지고
                      접근 할수 있는 기능.
        [i]   => i 번째 값
'''

surName = name[0] # name 문자열에서 첫 번째 문자를 변수에 저장
print("name[0] : ", surName)

print("city[-2] : ", city[-2]) # 리스트 city 에서 마지막 두번째 요소 출력

# 리스트의 마지막에서 네 번째 요소의 값을 변경
city[-4] = '서울특별시'
print("city : ", city)
# rint("city[5] : ",city[5]) # 리스트의 6번째 요소 갑 출력 -> 오류발생
                            # IndexError: list index out of range
                            
'''
2. 슬라이싱(slicing) :  시퀀스 자료형에서 일부를 잘라내어 
                       동일한 자료형으로
                       반환한느 기능.
[start : stop : step] => start에서 시작해서 stop 이전까지 step 간격으로 추출한다
'''
# 문자열의 1번지  부터 2번지 까지 잘라서 변수에 저장
giveName = name[1:3]
print("name[1:3] : ", giveName) # 성을 빼고 이름만 출력

# 리스트이 세번째 요소 부터 끝까지 출력
print("city [2:] : ", city [2:])

# 튜플의 두번째 요소부터 새번째 요소 까지 출력
print("num[1:3]", num[1:3])

# 튜플의 처음부터 끝까지 2씩 증가하면서 슬라이싱
print("num[::2]", num[::2])

# 인덱스 번위가 벗어났다. 하지만 가능한 값들만 자동 슬라이싱 한다.
print("num[-10:10]", num[-10:10])


'''
3. 연결 : + 연산자를 사용하여 두 개의 자료를 연결한다.
          새로운 시퀀스 자료형을 만든다.
자료형 + 자료형
'''

text1 = 'I Like'
text2 = text1 + 'Python Leanguage' # 문자열 + 문자열
print("text1 + 문자열 : ", text2)

num1 = (1, 2, 3, 4, 5)
num2 = (6, 7, 8, 9)
num = num1 + num2  # 튜플 + 튜풀

print("num1 + num2 : ", num)

# city(리스트) + num1(튜플)
#result = city + num1 # 요류 발생 서로 다른 자료형은 합칠 수 없다
#print("city + num1 : ", result)

'''
4. 반복 : * 연산자 사용한다
          시퀀스 자료형을 원하는 만큼 반복시킬 수 있는 기능
자료형 * 반복횟수
'''

# 튜플 생성
language = ('c', 'JAVA', 'Python')
# languag를 3번 반복하여 변수에 저장
languages= language * 3
print("languages : ",languages)

feel = 'happy' * 10
print('feel : ',feel)

contury = ['대한민국'] * 10
print("contury : ",contury)


'''
5. 맴버 유뮤 검사 : 시퀀스 자료형에 특정 자료가 있는지 알려주는 기능
자료 in 자료형
'''

color = ['red', 'green', 'blue', 'yellow']
print("리스트에 'black' 있나요?", 'black' in color)
print("리스트에 'red' 있나요?", 'red' in color)

text3 = 'Pyton'
print("t가 문자열에 있나요?", 't' in text3)
print("p가 문자열에 있나요?", 'p' in text3)
print("P가 문자열에 있나요?", 'P' in text3)

# in 연산자는 for 반복문에 효율적으로 사용
for i in text3 : # text3 안에 있는 문자를 하나씩 i 변수에 넣어서 반복
    print(i)
    

'''
6. 길이 정보 : 내장함수 len() 함수 사용한다
              시퀀스 자료형의 길이를 알 수 있다
len(자료형)
'''

# 문자열 text2 의 길이
print("text2의 길이 : ", len(text2))  # 22 => 띄어쓰기도 포함
# 리스트 city 의 길이
print("city의 길이 : ", len(city))