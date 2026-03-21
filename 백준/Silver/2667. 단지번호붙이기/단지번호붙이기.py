n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip())))

visited = [[False] * n for _ in range(n)]
count = 0
def dfs(x,y,visited):
    visited[x][y] = True
    global count
    count +=1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and arr[nx][ny] ==1:
                visited[nx][ny] = True
                dfs(nx,ny,visited)

    return count

apart = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            count = 0
            apart.append(dfs(i,j,visited))

apart.sort()
print(len(apart))
for i in range(len(apart)):
    print(apart[i], end='\n')