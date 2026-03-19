import sys
input = sys.stdin.readline

def solve():
    W = input().strip()
    K = int(input())
    
    if K == 1:
        print(1, 1)
        return

    # 1. 각 문자별로 인덱스 위치를 저장
    pos_dict = {}
    for i, char in enumerate(W):
        if char not in pos_dict:
            pos_dict[char] = []
        pos_dict[char].append(i)

    min_len = float('inf')
    max_len = -1

    # 2. 인덱스 리스트를 순회하며 K개씩 묶어 거리 계산
    for char, indices in pos_dict.items():
        if len(indices) < K:
            continue
            
        # 슬라이딩 윈도우: i번째부터 i+K-1번째 인덱스의 차이를 구함
        for i in range(len(indices) - K + 1):
            # 정확히 K개를 포함하는 구간의 길이
            length = indices[i + K - 1] - indices[i] + 1
            
            min_len = min(min_len, length)
            max_len = max(max_len, length)

    if max_len == -1:
        print(-1)
    else:
        print(min_len, max_len)

T = int(input())
for _ in range(T):
    solve()