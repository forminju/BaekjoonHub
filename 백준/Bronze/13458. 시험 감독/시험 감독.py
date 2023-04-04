n = int(input()) #5


minju = list(map(int, input().split())) #10 9 10 9 10

b,c = map(int, input().split()) #7 2

cnt =0

for i in range(len(minju)): #5

  if minju[i]>=b: 
    minju[i] = minju[i]-b # 3 2 3 2 3
    cnt+=1 # 5

    if minju[i]%c==0: # 나머지가 0이면
      cnt+=(minju[i]//c)

    else: # 나머지가 남아있으면
      cnt+=(minju[i]//c) +1

  else:
    cnt+=1    

print(cnt)      