def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x: x[1]) #진출지점 기준 정렬
    
    camera = -30001
    
    for i in range(0, len(routes)):
        if(camera < routes[i][0]):
            camera = routes[i][1]
            answer += 1
    
    return answer