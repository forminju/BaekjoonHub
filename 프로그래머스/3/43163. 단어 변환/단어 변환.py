from collections import deque

def solution(begin, target, words):
    def diff(word1, word2):
        diff_num = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_num +=1
        return diff_num
    
    queue = deque()
    queue.append((begin, 0))
    visited = [False] * len(words)
    
    while queue:
        current, count = queue.popleft()
        
        if current == target:
            return count
        
        for i in range(len(words)):
            if not visited[i] and diff(current, words[i]) == 1:
                visited[i] = True
                queue.append((words[i], count +1))
                
    return 0
                

            
    
