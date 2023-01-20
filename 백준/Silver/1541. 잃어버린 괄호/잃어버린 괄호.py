arr = input().split('-') # 50-45+30
#print(arr) # arr[0] = 50, arr[1]=45+30
# 50 / 45+30
# 45+30 에서 <+> 부터 계산!
pn = []
for i in arr:
  plus = 0
  for j in i.split('+'):
    plus+=int(j)
  pn.append(plus)
#print(pn) # 75  음...뭔가 잘못 됐다

n = pn[0] # 첫 번째 수 고정

#print(pn)
k = sum(pn[1:])

ans = n-k

print(ans)
  