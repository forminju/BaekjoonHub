from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    queue = deque()
    # queue.append((0,0))
    queue.append((numbers[0], 1))
    queue.append((-numbers[0], 1))
    
    while queue:
        tmp, idx = queue.popleft()
        
        if idx == n:
            if tmp == target :
                answer +=1
                
        else:
            queue.append((tmp+numbers[idx], idx+1))
            queue.append((tmp-numbers[idx], idx+1))
            
    return answer