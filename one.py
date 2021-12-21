def solution(progresses, speeds):
    answer = []
    queue = []
    
    for i in range(0, len(progresses)):
        if ((100-progresses[i]) % speeds[i] != 0):
            time = (100-progresses[i]) // speeds[i] + 1
            queue.append(time)
        else:
            time = (100-progresses[i]) // speeds[i]
            queue.append(time)
            
    front = 0
    value = 1
    for j in range(1, len(queue)):
        if queue[front]>=queue[j]:
            value += 1
        else:
            answer.append(value)
            front = j
            value = 1
    
    #아직 큐에 값 남아있다면 탈탈털기
    if(len(queue) > 0):
        answer.append(value)
    
    return answer