global answer
answer = 0

def solution(numbers, target):
    cnt = 0
    idx = 0
    
    def DFS(cnt, idx):
        global answer
        
        if idx == len(numbers):
            if cnt == target:
                answer += 1
        
        else:
            tmp_one = cnt + numbers[idx]
            tmp_two = cnt - numbers[idx]
            DFS(tmp_one, idx + 1)
            DFS(tmp_two, idx + 1)
    
    
    DFS(cnt, idx)
    
    return answer