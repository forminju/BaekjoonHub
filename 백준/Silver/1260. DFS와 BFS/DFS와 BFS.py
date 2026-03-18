import sys
from collections import deque

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)] # 1~n 까지 인덱스

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end= " ")

    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=" ")

        for i in graph[now]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)