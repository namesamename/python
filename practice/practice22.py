""" def profile(name, age, main_lang):
    print('이름: {0}\t 나이: {1}\t 주 사용 언어: {2}'.format(name,age,main_lang)) 

profile('가',20,'파이썬')
profile('나',25,'자바')"""


# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=19, main_lang='파이썬'):
    print('이름: {0}\t 나이: {1}\t 주 사용 언어: {2}'.format(name,age,main_lang))

profile('가')
profile('나')