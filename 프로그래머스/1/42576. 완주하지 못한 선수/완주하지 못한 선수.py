def solution(participant, completion):
    people = {}
    answer = []
    
    for i, part in enumerate(participant):
        if part not in people:
            people[part] = 1
        else:
            people[part] +=1
        
    for i,com in enumerate(completion):
        if com in people:
            people[com] -=1
            
    for i, p in enumerate(people):
        if people[p] > 0:
            answer.append(p)
            
    return ''.join(answer)