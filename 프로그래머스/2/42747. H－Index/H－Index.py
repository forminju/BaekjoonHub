def solution(citations):
    citations.sort()
    num_paper = len(citations)
    
    for i, cite in enumerate(citations):
        h = num_paper - i
        
        if cite >= h:
           return h
    
    return 0
