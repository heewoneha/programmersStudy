def solution(clothes):
    answer = 0
    
    what = {}
    
    for i in range(0, len(clothes)):
        what[clothes[i][1]] = []
    for i in range(0, len(clothes)):
        what[clothes[i][1]].append(clothes[i][0])
    
    a = []
    if (len(what.keys()) == 1):
        for key in what.keys():
            answer = len(what[key])
        
    else:
        for key in what.keys():
            a.append(len(what[key]))
    
        x = 1
        for i in a:
            x *= (i+1)
        
        answer = x - 1
            
    return answer