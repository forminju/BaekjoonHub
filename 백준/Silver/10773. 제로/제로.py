K = int(input())
stack = []

for _ in range(K):
    money = int(input())
    if money > 0:
        stack.append(money)
    if money == 0 :
        stack.pop()

print(sum(stack))
