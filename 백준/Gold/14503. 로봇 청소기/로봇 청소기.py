n,m = map(int,input().split())
r,c,d = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[0]*m for _ in range(n)]
clean_count = 0

while 1:
    if arr[r][c] == 0:
        arr[r][c] = 2
        clean_count += 1

    found_unclean = False
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if arr[nx][ny] == 0:
                found_unclean = True
                break

    if not found_unclean:
        bx, by = r-dx[d], c-dy[d]

        if 0<=bx<n and 0<=by<m and arr[bx][by] !=1:
            r,c = bx,by
        else:
            break
    else:
        d = (d+3) % 4
        nx, ny = r+dx[d], c+dy[d]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
            r,c = nx,ny

print(clean_count)