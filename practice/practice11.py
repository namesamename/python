cabinet={3:'가', 100:'나'}

""" print(cabinet[3])
print(cabinet.get(3)) """

""" print(cabinet[5]) #error
print(cabinet.get(5)) #none
print(cabinet.get(5, '사용 가능')) #5가 없을 경우 '사용 가능' 출력 """

print(3 in cabinet) #True
print(5 in cabinet) #False
