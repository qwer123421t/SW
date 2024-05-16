'''
   작성일 : 2024년 5월 16일
   작성자 : 컴퓨터공학과 202495001 강승훈
   설명 : 세트 : 중복을 허용하지 않는다.
'''
num = set()

# 3개의 숫자로 이루어진 세트
num1 = {2,1,3}
print("숫자 3개로 이루어진 세트 : ",num1) # 출력순서와 저장순서가 다르다

num2 = set([1,2,3,1,2])
print(num2) # 세트는 중복을 허용하지 않는다.

text = set("abcdefa")
print(text) # a 는 1개만 출력된다

num3 = {2,1,3}
#1이 num3에 있는가?
if 1 in num3 :
    print("1이 세트에 있습니다.")


num4 = {9,3,11,2,1,3,5,6,2}
print("num4 = ",num4)
#반복문으로 출력가능 => 중복제거.
for num in num4 :
    print(num,end=' ')
    
# 추가하기
num4.add(100)
print()
print("100추가",num4)

# 정렬하여 출력하기
for num in sorted(num4) :
    print(num, end=' ')
    
print()

# 삭제하기
num4.remove(100)
print("100삭제",num4)

# 세트의 연산
a = {1,2,3}
b = {1,2,3}

print("a == b",a == b)

num5 = {1,5,4,3,7,4}
print("num5 = ",num5)

print("num5의 길이 : ",len(num5)) # 중복을 제외하고 길이 찾아준다

print("num5 에서 최대값 : ",max(num5))
print("num5에서 최소값 : ",min(num5))
print("num5의 합계 : ",sum(num5))

A = {1,2,3}
B = {3,4,5}

# 합집합
# 합집합 연산 |
print("A | B", A | B)

#합집합 메소드 nuion()
print("A | B",A.union(B))

#교집합 
#교집합 연산 &
print("A & B", A & B)
#교집합 메소드 => Intersection()
print("A & B", A.intersection(B))

# 차집합 
# 차집합 => -
print("A - B", A - B)
# 차집합 메소드 => difference()
print("A - B", A.difference(B))

#대칭 차집합 => ^
print("A ^ B", A ^ B)