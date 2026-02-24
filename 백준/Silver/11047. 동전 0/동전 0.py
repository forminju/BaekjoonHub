import sys
input = sys.stdin.readline
 ##  목표는 k = 0

n,k = map(int, input().split())

coin = []

for i in range(n):
    coin.append(int(input().strip()))

coin.sort(reverse=True)
cnt = 0

for c in coin:
    if k == 0:
        break
    cnt += k // c # 나눈 몫을 count
    k%=c # 남은 것
    
print(cnt)
