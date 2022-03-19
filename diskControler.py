import heapq #디스크 컨트롤러(힙)

def solution(jobs):
    answer = 0; cur = 0
    heap = []
    
    tasks = sorted([(x[1], x[0]) for x in jobs], key = lambda x: (x[1], x[0]), reverse = True)
    heapq.heappush(heap, tasks.pop())
    
    while len(heap) > 0:
        leng, start = heapq.heappop(heap)
        cur = max(cur + leng, start + leng)
        answer += cur - start
        
        while(len(tasks)>0 and tasks[-1][1]<=cur):
            heapq.heappush(heap, tasks.pop())
        if len(tasks)>0 and len(heap)==0:
            heapq.heappush(heap, tasks.pop())
        
    return answer // len(jobs)