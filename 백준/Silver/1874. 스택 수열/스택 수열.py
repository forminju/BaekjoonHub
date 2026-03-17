n = int(input())
stack = []
answer = []
current = 1
is_number = True
for _ in range(n):
    number = int(input())

    while current <= number:
        stack.append(current)
        answer.append("+")
        current +=1

    if stack[-1] == number:
        stack.pop()
        answer.append("-")

    else:
        is_number = False
        break

if is_number:
    print("\n".join(answer))

else:
    print("NO")