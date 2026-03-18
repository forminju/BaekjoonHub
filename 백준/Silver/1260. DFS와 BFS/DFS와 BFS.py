from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
  queue = deque([v])    
  visit1[v] = 1   
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in range(1,n+1):
      if visit1[i] == 0 and graph[v][i] == 1:
        queue.append(i)
        visit1[i] = 1

def dfs(v):
  visit2[v] = 1        
  print(v, end = ' ')
  for i in range(1, n + 1):
    if visit2[i] == 0 and graph[v][i] == 1:
      dfs(i)

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit1 = [0] * (n + 1)
visit2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
