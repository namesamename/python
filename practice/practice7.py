python='Python is Amazing'

print(python.lower())
print(python.upper())
print(python[0].isupper()) #대괄호 속 자릿수의 글자가 대문자인지 확인
print(len(python)) #글자 수 확인
print(python.replace('Python', 'Java')) #치환

index=python.index('n') #문장 내 첫 번째 n의 자리를 찾는다
print(index)
index=python.index('n', index+1) #문장 내 두 번째 n의 자리를 찾는다
print(index)

print(python.find('n')) #index와 유사함

""" print(python.index('Java')) """ #error 발생
print(python.find('Java')) #존재하지 않아 -1로 나온다

print(python.count('n')) #문자가 몇 번 등장하는지 확인
