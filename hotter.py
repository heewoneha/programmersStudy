def solution(scoville, K):
    answer = 0
    #부모 인덱스 (i-1)//2
    #왼쪽 자식 인덱스 i*2+1
    #오른쪽 자식 인덱스 i*2+2
    
    
    while(min(scoville) < K): #0으로 하면 안되는 이유는 아직 정렬 안해서
        scoville.sort()
        if (len(scoville) < 2):
            return -1
        
        a = scoville[0]
        b = scoville[1]

        mix_sco = a + b * 2
            
        scoville = scoville[2:len(scoville)]
        scoville.insert(0, mix_sco)
            
        answer += 1
        
    return answer