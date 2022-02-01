def solution(n, lost, reserve): #x번째-1 == 인덱스
    answer = 0
    
    dress = []
    for i in range(0, n):
        dress.append(1)
        if ((i+1) in reserve):
            dress[i] += 1
        if ((i+1) in lost):
            dress[i] -= 1

    for j in range(0, n):
        if (dress[j] == 0):
            if ((j-1) > -1 and (dress[j-1] == 2)):
                dress[j-1] -= 1
                dress[j] += 1
            elif ((j+1) < len(dress) and (dress[j+1] == 2)):
                dress[j+1] -= 1
                dress[j] += 1
    
    answer += dress.count(1)
    answer += dress.count(2)
    
    return answer