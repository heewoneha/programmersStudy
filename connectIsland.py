def solution(n, costs): # 섬 연결하기(그리디)
    answer = 0
    
    costs.sort(key=lambda x:x[2]) # 비용기준 오름차순 정렬
    
    routes = set([costs[0][0]])
    while (n != 0): # 최종 초록색 간선 개수는 n-1개, 혹은 while len(routes)!=n 도 가능
        for i, cost in enumerate(costs):
            if (cost[0] in routes) and (cost[1] in routes):
                continue
            if (cost[0] in routes) or (cost[1] in routes):
                routes.update([cost[0], cost[1]]) # set 자체에서 중복제거, 이미 다른 점에 의해서 간선 다 연결된 점일 경우를 대비해 이렇게 추가
                answer += cost[2] # 비용 append
                del(costs[i])
                break
        n -= 1

    return answer