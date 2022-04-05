""" # 리스트

# 지하철 칸별로 10명, 20명, 30명
subway=[10,20,30]
print(subway)

subway=['가나다','라마바','사아자']
print(subway)

# 사아자는 몇 번째 칸에 타고 있는가?
print(subway.index('사아자'))

# 차카타가 다음 정류장에서 다음 칸에 탑승
subway.append('차카타')
print(subway)

# 파하를 가나다와 라마바 사이에 태운다
subway.insert(1,'파하')
print(subway)

# 한 명씩 뒤에서 꺼낸다
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append('가나다')
print(subway)
print(subway.count('가나다')) """



 # 리스트 정렬

# 오름차순
num_list=[5,2,4,3,1]
""" num_list.sort()
print(num_list)

# 위(오름차순)의 역순
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list) """



# 다양한 자료형 함께 사용
mix_list=['가나다',20,True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)