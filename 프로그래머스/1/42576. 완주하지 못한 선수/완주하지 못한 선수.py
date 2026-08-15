def solution(participant, completion):
    people = {}
    answer = []
    
    for part in participant:
        if part in people:
            people[part] +=1
        else:
            people[part] = 1
            
    for com in completion:
            people[com] -=1
            
    for name in people:
        if people[name] > 0:
            answer.append(name)
            
    return ''.join(answer)