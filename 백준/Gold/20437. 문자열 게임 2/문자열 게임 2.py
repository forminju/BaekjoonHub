import sys
input = sys.stdin.readline

def solve():
    W = input().strip()
    K = int(input())
    pos_dict = {}

    for i, char in enumerate(W):
        if char not in pos_dict:
            pos_dict[char] = []
        pos_dict[char].append(i) # 숫자에 대한 위치 조정

    max_len = -1
    min_len = float('inf')

    for char, indices in pos_dict.items():
        if len(indices) < K:
            continue

        for i in range(len(indices)-K+1):
            length = indices[i+K-1] - indices[i] + 1
            max_len = max(max_len, length)
            min_len = min(min_len, length)

    if max_len ==-1:
        print(-1)

    else:
        print(min_len, max_len)


T = int(input())
for _ in range(T):
    solve()