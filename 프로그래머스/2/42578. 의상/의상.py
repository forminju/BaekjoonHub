def solution(clothes):
    clothes_set = {}
    
    for cloth in clothes:
        category = cloth[1]
        
        if category in clothes_set :
            clothes_set[category] +=1
        else:
            clothes_set[category] = 1
            
            
    answer = 1
    
    for category in clothes_set:
        answer *= clothes_set[category] + 1
        
    return answer -1