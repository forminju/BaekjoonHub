N = int(input())
top = list(map(int, input().split()))
stack = [] # [번호, 높이] -> stack 에 이렇게 들어갈 수 있는 거 확인.
answer = []

for i in range(N):
    h = top[i] # 현재 상황 체킹

    while stack and stack[-1][1] < h:
        stack.pop()

    if stack:
        answer.append(stack[-1][0])

    else:
        answer.append(0)

    stack.append([i+1,h])


print(" ".join(map(str, answer)))

