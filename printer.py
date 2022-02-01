def solution(priorities, location):
    answer = 0
    
    cnt = 1
    while(priorities):
        if (location == 0):
            if(priorities[0] >= max(priorities)):
                priorities.pop(0)
                answer = cnt
                break
                
            else:
                tmp = priorities.pop(0)
                priorities.append(tmp)
                location = len(priorities) - 1
                
        else:
            if(priorities[0] >= max(priorities)):
                priorities.pop(0)
                cnt += 1
                location -= 1
                
            else:
                tmp = priorities.pop(0)
                priorities.append(tmp)
                location -= 1
    
    return answer