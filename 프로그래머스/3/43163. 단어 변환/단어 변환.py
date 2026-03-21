from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    def diff(word1, word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count +=1
        return count
    
    def bfs(begin, target):
        n = len(words)
        queue = deque([(begin, 0)])
        visited = [False] * n
        
        while queue:
            tmp, count = queue.popleft()
            
            if tmp == target:
                return count
            
            for i in range(len(words)):
                if not visited[i] and diff(words[i], tmp) ==1:
                    visited[i] = True
                    queue.append((words[i], count+1))
                    
        
        return 0
    
    return bfs(begin, target)