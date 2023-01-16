n = int(input())
m = input()
countS =0
countL = 0
ans = 0

for i in range(n):
  if m[i] == 'L':
    countL+=1
  else:
    countS +=1

ans = countL//2+countS+1

ansf = min(n, ans)

print(ansf)