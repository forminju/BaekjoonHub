from collections import Counter

K = Counter(input()) # dared 문자열 빈도수 확인
M = Counter(input()) # bread 문자열 빈도수 확인

#print(sum(K.values()))
#print(sum(M.values()))
#print(sum((K-M).values()))
#print(sum((M-K).values()))
#1. dared -> d : 2 a : 1 r : 1 e : 1 Counter(input())
#2. bread -> b : 1 d : 1 r : 1 e : 1 a :1
# d / b 제거 필요


print(sum((K-M).values())+sum((M-K).values()))
# sum(K-M)
