from collections import deque
n = int(input())
a,b = map(int,input().split())
t = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(t):
    u,v = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0] * (n+1)

def bfs(a,b):
    queue = deque([a])
    visited[a] = 1

    while queue:
        v = queue.popleft()

        if v == b:
            return visited[b] -1

        for w in arr[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1 # 현재에서 한 칸 더!  가는 것
                queue.append(w)

    return -1

print(bfs(a,b))