import math

def solution(progresses, speeds):
    answer = []
    
    days = []
    for i in range(0, len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    count = 0
    maximum = days[0]
    for i in range(0, len(days)): # 0부터 시작하는 아이디어
        if maximum < days[i]:
            answer.append(count)
            maximum = days[i]
            count = 0
            
        count += 1
    
    if count > 0:
        answer.append(count)
    
    return answer