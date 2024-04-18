'''
[문제분석]
    초미새먼지 농도에 따른 문자 메세지 발송
    좋음 : 15 미만
    보통 : 15 ~ 35
    나쁨 : 35 초과
[알고리즘]
    1. 초미세먼지 농도를 측정한다.(입력 받는다.)
    2. 만약 초미세먼지 농도가 15 미만이면
        2-3 좋음
    3. 만약 초미세먼지 농도가 15 ~ 35 이면 
        3-1 보통
    4. 만약 초미세먼지 농도가 35 초과이면
        4-1. 나쁨
'''
dust = int(input("초미새먼지 농도를 입력해주세요. : "))
if dust < 15 :
    print("좋음")
if 15 <= dust <= 35 : # dust >= 15 and dust <= 35
    print("보통")
if dust > 35 :
    print("나쁨")

if mise < 15 :
    print("좋음")
elif 15 <= mise <= 35 :
    print("보통")
else :
    print("나쁨")
    

if mise < 15 :
    print("좋음")
elif mise <= 35 :
    print("보통")
else :
    print("나쁨")

if mise < 15 :
    print("좋음")
elif mise > 35 :
    print("나쁨")
else :
    print("보통")   