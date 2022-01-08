import heapq #in C++, use <queue> - priority queue

def solution(scoville, K):
    answer = 0
    
    priority_queue = []
    for value in scoville:
        heapq.heappush(priority_queue, value)
    
    while (priority_queue[0] < K):
        if(len(priority_queue) > 1):
            heapq.heappush(priority_queue, heapq.heappop(priority_queue) + heapq.heappop(priority_queue) * 2)
        else:
            return -1
        answer += 1
    
    return answer