from calendar import c


cabinet={3:'가', 100:'나'}

""" print(cabinet[3])
print(cabinet.get(3)) """

""" print(cabinet[5]) #error
print(cabinet.get(5)) #none
print(cabinet.get(5, '사용 가능')) #5가 없을 경우 '사용 가능' 출력 """

""" print(3 in cabinet) #True
print(5 in cabinet) #False """

cabinet={'a-3':'가','b-100':'나'}
print(cabinet['a-3'])
print(cabinet['b-100'])

print(cabinet)
cabinet['a-3']='라'
cabinet['c-20']='다'
print(cabinet)

del cabinet['a-3']
print(cabinet)

print(cabinet.keys()) #key 전체 출력
print(cabinet.values()) #value 전체 출력
print(cabinet.items()) #key, value 전체 출력

cabinet.clear()
print(cabinet)