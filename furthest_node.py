from collections import deque

def solution(n, edge):
    def bfs(v):
        count = 0
        q = deque()
        q.append([v, count])

        while(q):
            x = q.popleft()
            v = x[0]
            count = x[1]
            if visit[v] == -1:
                visit[v] = count
                count += 1
                for e in adj[v]:
                    q.append([e, count])
    
    answer = 0
    adj = [[] for _ in range(n+1)]
    visit = [-1] * (n+1)
    
    for x, y in edge:
        adj[x].append(y) #node
        adj[y].append(x)
    
    bfs(1)
    
    for val in visit:
        if val == max(visit):
            answer += 1
    
    return answer

#print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))