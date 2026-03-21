n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().strip())))

visited = [[False] * n for _ in range(n)]
apart = []

def dfs(x,y, visited):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = True
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                count += dfs(nx,ny,visited)

    return count

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            house_count = dfs(i,j,visited)
            apart.append(house_count)

print(len(apart))
for count in sorted(apart):
    print(count)

