def solution(max_weight, specs, names):
    answer = 1
    
    dic = {}
    for i in range(0, len(specs)):
        dic[specs[i][0]] = int(specs[i][1])
    
    
    sum_all = 0
    for i in range(0, len(names)):
        sum_all += dic[names[i]]
        if sum_all > max_weight:
            answer += 1
            sum_all = dic[names[i]]
            
    return answer