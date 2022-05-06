# 단어변환 (DFS)
def isOneDiff(a, b): #두 단어에서 다른 개수 1개인가 확인
    cnt = 0
    for _ in range(0, len(a)):
        if (a[_] != b[_]):
            cnt += 1
            
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 50
    visited = [0] * 50
    
    def DFS(begin, target, words, ptr):
        nonlocal answer #부모 함수 값. global은 여기서 사용 불가
        if answer <= ptr:
            return
        if begin == target:
            answer = min(answer, ptr)
            return
        
        for i in range(0, len(words)):
            if isOneDiff(begin, words[i]) and not visited[i]:
                visited[i] = 1
                DFS(words[i], target, words, ptr+1)
                visited[i] = 0 #백트래킹
        return
    
    DFS(begin, target, words, 0)
    if (answer == 50): #target 도달 실패
        return 0
    
    return answer