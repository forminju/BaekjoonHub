import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
connect = int(input())

graph = [[] for _ in range(n+1)]

chk = [False]*(n+1)
cnt =0

for i in range(connect):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)




def bfs(graph, v):
    global cnt
    queue=deque([v])

    while queue:
        pop = queue.popleft()
        chk[pop]= True

        for i in graph[pop]:
            if chk[i]==False:
                chk[i]=True
                queue.append(i)
                cnt+=1
    print(cnt)

bfs(graph,1)
