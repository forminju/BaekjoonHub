N = int(input())

stack = []

for _ in range(N):
    word = input().split()
    command = word[0]

    if command == 'push':
        stack.append(word[1])

    elif command == 'pop':
        if stack:
            answer = stack.pop()
            print(answer)
        else:
            print(-1)

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    elif command == 'top':
        if stack:
            answer = stack[-1]
            print(answer)
        else:
            print(-1)
