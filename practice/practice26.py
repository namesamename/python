# 표준 입출력



""" print('python','java',sep=',',end='?')
print('무엇이 더 재미있을까요?') """

""" import sys
print('python','java',file=sys.stdout) #표준 출력
print('python','java',file=sys.stderr) #표준 에러 """

""" scores={'수학': 0, '영어': 50, '코딩': 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=':') #ljust: 왼쪽 정렬, rjust: 오른쪽 정렬, 괄호 안 숫자는 공백 칸 수 """

""" for num in range(1,21):
    print('대기번호: '+str(num).zfill(3)) #0을 채운다. 괄호 안 숫자는 자리수 """

answer=input('아무 값이나 입력하세요: ') #input 값은 문자열로 들어온다.
# print(type(answer))
print('입력하신 값은 '+answer+'입니다.')