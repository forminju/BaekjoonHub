n = int(input())
li = list(map(int, input().split())) # [1 5 7 9]

li.sort() #[1 5 7 9]

print(li[(n-1)//2])
  