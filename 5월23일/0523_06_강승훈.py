'''
   작성일 : 2024년 5월 23일
   작성자 : 컴퓨터공학과 202495001 강승훈
   설명 : readline() 메소드 사용법
'''
print("=======readline() 메소드 이용하여 읽기 ===========")

# with open을 이용하여 읽기 모드로 파일 객체 생성.
with open("test2.txt","r") as f :
    # while 문을 사용하여 무한 반복
    while True :
       line = f.readline() # 한 줄씩 읽어와 변수에 저장 
       print(line)
       if line == '' : # 읽어 온 값이 없는 경우 반복을 벗어난다
        break
        
    


# with open을 사용하면 f.close() 쓸 필요 없다