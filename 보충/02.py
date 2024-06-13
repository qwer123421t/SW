'''
     학번을 입력받아 어느 학과 학생인지 알려주세요.
    학번은 학과 코드 영문자와 숫자로 구성되어 있습니다.

    예) C202095001
    [학과 코드]
    C : 컴퓨터공학과  A : 인공지능공학과   F : 식품영양학과

    입력받는 학과코드는 대소문자를 구분하지 않습니다.
    학과를 알려주는 부분은 함수로 작성하세요.

    [출력 결과]
        [학과 코드]
         C : 컴퓨터공학과 , A : 인공지능공학과, F : 식품영양학과
        학번을 입력하세요 : c202095001 
        c202095001학생은 컴퓨터공학과 소속입니다.

        학번을 입력하세요 : A202045001
        A202045001학생은 컴퓨터공학과 소속입니다.

        학번을 입력하세요 : s202036001
        해당 학과는 없습니다.
'''
'''
school_num = input('학과코드를 입력해주세요 : ')

if 'c' in school_num or 'C' in school_num :
    print(f'{school_num}학생은 컴퓨터공학과소속입니다.')
elif 'a' in school_num or 'A' in school_num :
    print(f'{school_num}학생은 인공지능공학과소속입니다.')
elif 'f' in school_num or 'F' in school_num :
    print(f'{school_num}학생은 식품영양학과소속입니다.')
else :
    print('해당 학과는 없습니다.')
'''
def Dept(school_num) :
    if 'c' in school_num or 'C' in school_num :
        print(f'{school_num}학생은 컴퓨터공학과소속입니다.')
    elif 'a' in school_num or 'A' in school_num :
        print(f'{school_num}학생은 인공지능공학과소속입니다.')
    elif 'f' in school_num or 'F' in school_num :
        print(f'{school_num}학생은 식품영양학과소속입니다.')
    else :
        print('해당 학과는 없습니다.')

print('[학과코드]')
print('C : 컴퓨터공학과, A : 인공지능공학과, F : 식품영양학과')
print()
school_num = input('학과코드를 입력해주세요 : ')

# startswitch(시작하는 문자)
# endswitch(끝나는 문자)

if school_num.startswith('c') or school_num.startswith('C') :
    print(f'{school_num} 학생은 컴퓨터공학과 입니다.')
elif school_num.startswith('a') or school_num.startswith('A') :
    print(f'{school_num} 학생은 인공지능학과 입니다.')
elif school_num.startswith('f') or school_num.startswith('F') :
    print(f'{school_num} 학생은 식품영양학과 입니다.')