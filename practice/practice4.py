from random import *

print(random()) #0.0~1.0 임의의 값
print(random()*10) #0.0~10.0 임의의 값

print(int(random()*10)) #0~10(미만=9) 임의의 값
print(int(random()*10)+1) #1~10(이하=10) 임의의 값

print(int(random()*45)+1) #로또 당첨 번호 중 생성(1~45)
print(int(random()*45)+1) #로또 당첨 번호 중 생성(1~45)
print(int(random()*45)+1) #로또 당첨 번호 중 생성(1~45)
print(int(random()*45)+1) #로또 당첨 번호 중 생성(1~45)
print(int(random()*45)+1) #로또 당첨 번호 중 생성(1~45)
print(int(random()*45)+1) #로또 당첨 번호 중 생성(1~45)

print(randrange(1,46)) #1~46(미만=45) 임의의 값

print(randint(1,45)) #1~45(이하=45) 임의의 값