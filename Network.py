from collections import deque
def solution(n, computers):
    
    def BFS(root):
        q = deque()
        q.append(root)
        
        while(q):
            x = q.popleft()
            visited[x] = True
            for j in range(root, n):
                if (computers[x][j] and not(visited[j])):
                    q.append(j)
                    
                    
    answer = 0
    visited = [False for i in range(0, n)]
    for i in range(0, n):
        if not (visited[i]):
            BFS(i)
            answer += 1
        
    return answer