# 집합(set)
# 중복, 순서 X

my_set={1,2,3,3,3}
print(my_set)

java={'가','나','다'}
python=set(['가','라'])

# 교집합 (java와 python 모두 가능한 개발자)
print(java&python)
print(java.intersection(python))

# 합집합 (java 혹은 python 가능한 개발자)
print(java|python)
print(java.union(python))

# 차집합 (java만 가능한 개발자)
print(java-python)
print(java.difference(python))

# python 개발자 증가
python.add('나')
print(python)

# java -> python 이직 개발자
java.remove('나')
print(java)