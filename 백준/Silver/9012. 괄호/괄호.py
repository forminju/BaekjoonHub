N = int(input())

for _ in range(N):
    arr = input()
    stack = []
    is_vps = True

    for str in arr:
        if str == '(':
            stack.append(str)
        elif str == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break

    if is_vps and not stack:
        print("YES")
    else:
        print("NO")
