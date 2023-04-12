def solution(v):
    answer = []

    dic_x = {}
    dic_y = {}
    
    for i in range(0, len(v)):
        if v[i][0] not in dic_x.keys():
            dic_x[v[i][0]] = 1
        else:
            dic_x[v[i][0]] += 1
        
        if v[i][1] not in dic_y.keys():
            dic_y[v[i][1]] = 1
        else:
            dic_y[v[i][1]] += 1
    
    
    rect_x = list(zip(dic_x.keys(), dic_x.values()))
    rect_y = list(zip(dic_y.keys(), dic_y.values()))
    
    for i in range(0, len(rect_x)):
        if rect_x[i][1] == 1:
            answer.append(rect_x[i][0])
    
    for i in range(0, len(rect_y)):
        if rect_y[i][1] == 1:
            answer.append(rect_y[i][0])
        
            
    return answer