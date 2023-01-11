import sys

A = int(input())
li = [0]*10001

for i in range(A):
    N = int(sys.stdin.readline())
    li[N] +=1


for i in range(10001):
    if li[i]!=0:
        for j in range(li[i]):
            print(i)