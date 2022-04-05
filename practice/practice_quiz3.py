""" naver='http://naver.com'
naver=naver[7:]
dot=int(naver.index('.'))
naver=naver[:dot]
naverlen=len(naver)
navere=naver.count('e')
naver=naver[:3]

print(naver+str(naverlen)+str(navere)+'!') """

url='http://naver.com'
my_str=url.replace('http://','')
my_str=my_str[:my_str.index('.')]
pw=my_str[:3]+str(len(my_str))+str(my_str.count('e'))+'!'

print('{0}의 비밀번호는 {1}입니다.'.format(url, pw))