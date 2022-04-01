
name=input('성함을 입력해주세요.')
height=input('신장을 입력해주세요.')
height=int(float(height))
weight=float(input('체중을 입력해주세요.'))

print('''신장: {}cm
체중: {}kg'''.format(height,weight))

bmi=weight/(height/100)**2

print('BMI 지수는 {0:.1f}입니다.'.format(bmi))

input('엔터를 눌러야 종료됩니다.')
