n = int(input()) # 3 -> 3x3 그래프 생성
graph = [list(map(int, input().split())) for _ in range(n)]
#print(graph)
# 쩰리는 오른쪽, 아래로만 이동 가능
visited = [[0]*n for _ in range(n)]

def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=n or visited[x][y]==1:
    return 

  if graph[x][y] ==-1:
    visited[x][y]=1
    return

  visited[x][y]=1 


  dfs(x+graph[x][y], y)
  dfs(x-graph[x][y], y)
  dfs(x, y+graph[x][y])
  dfs(x, y-graph[x][y])

# 쩰리 : (0x0) -> (nxn) 칸에 도달해야 승리


dfs(0,0)

if visited[-1][-1] ==1 :
  print("HaruHaru")
else :
  print("Hing")  
