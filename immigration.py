def solution(n, times):
    answer = 0
    times.sort()
    
    left = 1
    right = times[len(times) - 1] * n #worst time, max*n
    
    while (left < right): #binary search
        mid = (left + right) // 2; sum_all = 0 #available people
        for t in times:
            sum_all += (mid // t)
            
        if sum_all >= n:
            right = mid
        else:
            left = mid + 1 #more time
            
    answer = left
    return answer
