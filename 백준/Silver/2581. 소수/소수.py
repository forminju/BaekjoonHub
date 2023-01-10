n = int(input())
m = int(input())

li = []

for i in range(n,m+1):
  for j in range(2, i+1):
    if i == j:
      li.append(i)
    if i%j==0:
      break  

li.sort()

if len(li)>0:
  print(sum(li))
  print(li[0])

else:
  print(-1)  