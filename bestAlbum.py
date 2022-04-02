def solution(genres, plays): #베스트 앨범(해시)
    answer = []
    dic = {}
    
    gen_play = list(zip(genres, plays))
    for gen, pla in gen_play:  #장르별 총 재생횟수 dict
        dic[gen] = dic.get(gen, 0) + pla
        
    dic = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    enu = list(enumerate(gen_play))

    enu.sort(key = lambda x : x[1], reverse = True) #조건맞게 정렬
    
    for i in dic:
        cnt = 0
        for j in enu:
            if cnt == 2:
                break
            if i[0] == j[1][0]:
                answer.append(j[0])
                cnt += 1
    
    return answer