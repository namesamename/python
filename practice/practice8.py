""" print('a'+'b')
print('a','b') """

# 방법 1
""" print('나는 %d살입니다.' %20) #d=정수
print('나는 %s을 좋아해요.' %'파이썬') #s=문자열(정수와 문자 무관하게 출력 가능)
print('Apple은 %c로 시작해요.' %'A') #c=Character=한 글자 문자

print('나는 %s살입니다.' %20)
print('나는 %s색과 %s색을 좋아해요.' %('파란','빨간')) """


# 방법 2
""" print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란','빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란','빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란','빨간'))
print('나는 {1}색과 {3}색을 좋아해요.'.format('파란','빨간','노란','하얀')) """

# 방법 3
""" print('나는 {age}살이고, {color}색을 좋아해요.'.format(age=20, color='빨간'))
print('나는 {age}살이고, {color}색을 좋아해요.'.format(color='빨간', age=20)) """

# 방법 4 (v3.6 이상)
age=20
color='빨간'
print(f'나는 {age}살이고, {color}색을 좋아해요.')