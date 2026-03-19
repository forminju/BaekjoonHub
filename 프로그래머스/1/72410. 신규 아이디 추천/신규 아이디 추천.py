def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    
    for char in new_id:
        if char.isdigit() or char.isalpha() or char in ['-', '_', '.']:
            answer += char
            
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    answer = answer.strip('.')
        
    if answer == '':
        answer = 'a'
        
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] =='.':
            answer = answer[:-1]
            
            
    while len(answer) <3 : 
            answer += answer[-1]
            
    return answer
        