from collections import deque

def bfs(si, sj, ei, ej):
    queue = deque([(si,sj)])
    visited = [[0] * m for _ in range(n)]
    visited[si][sj] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        ni, nj = queue.popleft()

        if ni == ei and nj == ej:
            return visited[ei][ej]

        for i in range(4):
            nx = ni + dx[i]
            ny = nj + dy[i]

            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = visited[ni][nj] +1

n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
print(bfs(0,0,n-1,m-1))