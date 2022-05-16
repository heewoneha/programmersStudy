from collections import deque #다리를 지나는 트럭(큐)
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    idx = 0
    sum = 0
    q = deque()
    
    while(True):
        if (idx == len(truck_weights)): #마지막 트럭 하나
            answer += bridge_length
            break
        
        answer += 1
        tmp = truck_weights[idx]
        
        if (len(q) == bridge_length): #트럭 다 건넘
            sum -= q.popleft()
        
        if (sum + tmp <= weight): #현재 다리에 다음 트럭 가능
            sum += tmp
            q.append(tmp)
            idx += 1
        else: #현재 다리에 다음 트럭 불가능.
            q.append(0)
            
    return answer