def solution(citations):
    citations.sort()
    n = len(citations)
    
    for i, cite in enumerate(citations):
        if cite >= n-i:
            return n-i
        
    return 0