def solution(today, terms, privacies):
    answer = []
    
    hs = {}
    
    for t in terms:
        typ, due_mon = t.split()
        hs[typ] = int(due_mon) * 28 
        
    def to_days(today):
        y,m,d = list(map(int, today.split('.')))
        revised_day = (y*12*28) + (m*28) + d
        
        return revised_day
    
    revised_tday = to_days(today)
    
    for i, prv in enumerate(privacies):
        date, typ = prv.split()
        
        expire_total = to_days(date) + hs[typ]
        
        if expire_total <= revised_tday :
            answer.append(i+1)

    return answer