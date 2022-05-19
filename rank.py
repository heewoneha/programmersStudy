def solution(n, results): #순위<그래프>, 플로이드 와샬
    answer = 0
    
    g = [[False for col in range(n+1)] for row in range(n+1)]
    
    for x in range(0, len(results)):
        g[results[x][0]][results[x][1]] = True
    
    for x in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if g[i][x] and g[x][j]:
                    g[i][j] = True
    
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if g[i][j] or g[j][i]:
                cnt += 1
        if cnt == n-1:
            answer += 1
    
    return answer