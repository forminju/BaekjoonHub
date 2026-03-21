def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(computer, v, visited):
        visited[v] = True # v 나를 기준으로 돌아가자.
        # v번 컴퓨터와 연결된 다른 컴퓨터 모두 확인
        for i in range(n):
            if computer[v][i] == 1 and not visited[i]:
                dfs(computer, i, visited)
            
                
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            answer +=1
            
    return answer