# continue and break

absent=[2,5] #결석
noBook=[7] #교과서 없음
for student in range(1,11):
    if student in absent:
        continue
    elif student in noBook:
        print('오늘 수업은 여기까지다. {}는 교무실로 따라 와.'.format(student))
        break
    print('{}, 책을 읽어봐.'.format(student))