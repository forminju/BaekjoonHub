from collections import deque

n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().strip())))

visited = [[False] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 새로운 단지 찾을 때마다 queue 재사용

count = 0
def bfs(si, sj):
    global count
    queue = deque([(si,sj)])
    visited[si][sj] = True
    count +=1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    count += 1
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return count

apart = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            count = 0
            apart.append(bfs(i,j))

apart.sort()

print(len(apart))
for i in range(len(apart)):
    print(apart[i], end='\n')