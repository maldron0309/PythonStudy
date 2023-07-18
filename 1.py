# -*- coding: utf-8 -*-

# -- Sheet --

print("Hello, World!")

# 주석은 #
print(1+4)
print(9-3)
print(12*7)
print(23/4)

# 변수 -> 값을 저장하는 저장공간의 이름, 대소문자 구분한다
# 한글변수 이름 가능하다
# 첫글자는 숫자, 특수문자 (_는 가능) 불가, 키워드는 변수이름 불가능

a = 1234
print(a * 2)

a = "박진형"
print(a*10)

#문자열 - " " / ' ' 
str1 = "abcd"
str2 = "efgh"

print(str1)
print(str2)

str1 + str2

str2 + str1

# **indexing : 문자열의 각 자리의 인덱스 번호**


str1[0]

# **slicing : 지정한 범위를 잘라내는 동작**    


print(str1[0:3])
print(str1[0:])
print(str1[:2])
print(str1[1:-1])



