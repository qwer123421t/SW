'''
   작성일 : 2024년 5월 16일
   작성자 : 컴퓨터공학과 202495001 강승훈
   설명 : 다음과 같은 튜플을 생성하고,
          각 요소(숫자)가 튜플에 몇 개 있는지를 출력하시오.
          
          len(),  count(),   0번지 부터
          
          개수를 찾은 숫자는 리스트에 따로 저장한다.
          이미 찾은 숫자는 또 개수를 찾을 필요가 없다.
'''
# 튜플 생성
num = (4,1,3,6,5,7,9,5,1,4,6,0,1,2,7,8,9)
print("생성된 튜플 : ",num)

for i in range(len(num)) :
    print(num[i],"의 개수는 : ",num.count(num[i]))
    # => 중복하여 숫자의 개수가 다 출력된다
    
print()
print("중복 제거하고 개수 찾기")

num_list =[] # 중복 출력 하지 않기 위한 빈  리스트

# 리스트에 숫자가 있는지 없는지 판단
# 만약 숫자가 리스트에 있는으면 패스
#ㅇ없으면 개수 찾고, 리스트에 추가 => 다음 수가 있는지 체크
for i in range(len(num)) :
    if num[i] in num_list :
        continue # 반복의 처음으로 돌아가시오
    else :
        print(num[i],"의 개수는 : ",num.count(num[i]))
        num_list.append(num[i]) # 리스트에 추가
        
print()
num_list =[]  # 다시 초기화
for i in range(len(num)) :
    if num[i] not in num_list :
        print(num[i],"의 개수는 : ",num.count(num[i]))
        num_list.append(num[i]) # 리스트에 추가