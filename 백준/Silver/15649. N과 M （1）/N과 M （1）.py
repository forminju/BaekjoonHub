import sys
input = sys.stdin.readline

def dfs(n, lst):
    # 종료 조건  (n에 관련된) + 정답 처리
    if n == M:
        ans.append(lst)
        return

    # 하부 단계 (함수) 호출
    for j in range(1, N+1):
        if visited[j] == 0:
            visited[j] = 1
            dfs(n+1, lst +[j])
            visited[j] = 0

N, M = map(int, input().split())
ans = []
visited = [0] * (N+1)
dfs(0, [])

for lst in ans:
    print(*lst)
    # print(' '.join(map(str. lst)))