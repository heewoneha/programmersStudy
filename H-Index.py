def solution(citations): #O(N^2) - 나중에 다시 풀기
    answer = 0
    
    ind = [] #인덱스 리스트 추가
    for i in range(0, len(citations)):
        ind.append(i + 1)
    
    citations.sort(reverse = True)

    if citations[-1] == citations[0] == 0: #모두 같은 수, 0
        return answer
    
    for i in range(0, len(citations)):
        cnt_one = 0
        cnt_two = 0
        
        #h번 이상 인용 개수
        for num in citations:
            if num >= (i+1):
                cnt_one += 1
                
        #h번 이하 인용 개수
        for num in citations:
            if num <= (i+1):
                cnt_two += 1
                
        if (cnt_one >= (i+1)) and (cnt_two <= (i+1)):
            answer = i+1
    
    return answer