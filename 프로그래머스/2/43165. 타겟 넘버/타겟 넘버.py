from collections import deque

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    queue = deque(([numbers[0],0], [-numbers[0],0]))
    
    while queue:
        tmp, idx = queue.popleft()
        idx +=1
        if idx == n:
            if tmp == target:
                answer +=1
        else:
            queue.append((tmp+numbers[idx], idx))
            queue.append((tmp-numbers[idx], idx))
                
    return answer