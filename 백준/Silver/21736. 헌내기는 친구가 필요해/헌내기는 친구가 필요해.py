import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline



def dfs(x,y):
    global cnt
    visited[x][y] = True
    
    if campus[x][y] =='P':
        cnt +=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if campus[nx][ny]!='X':
                dfs(nx, ny)
        
        
        

n,m = map(int, input().split())
campus = []

for _ in range(n):
    campus.append(list(map(str, input())))
    
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if campus[i][j] =='I':
            dfs(i,j)
    

if cnt== 0 :
    print('TT')
    
else :
    print(cnt)