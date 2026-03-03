num = []
for _ in range(3):
    num.append(int(input()))

targer_num = num[0] * num[1] * num[2]
target_str = str(targer_num)

ans = [0] * 10

for ch in target_str:
    ans[int(ch)] +=1

for i in range(10):
    print(ans[i])
