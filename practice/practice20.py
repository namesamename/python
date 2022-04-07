# 한 줄 for

# 1,2,3,4,5번이었던 출석 번호를 101,102,103... 식으로 변경
students=[1,2,3,4,5]
print(students)
students=[i+100 for i in students]
print(students)


# 학생 이름을 길이로 변환
students=['iron man','thor','groot']
students=[len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students=['iron man','thor','groot']
students=[i.upper() for i in students]
print(students)