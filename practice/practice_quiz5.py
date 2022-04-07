from random import *

count=0
for i in range(1, 51):
    time=randrange(5,51)
    if 5<=time<=15: #매칭 성공
        print('[O] {0}번째 손님 (소요시간: {1}분)'.format(i,time))
        count+=1
    else: #매칭 실패
        print('[ ] {0}번째 손님 (소요시간: {1}분)'.format(i,time))

print('총 탑승 승객: {}분'.format(count))