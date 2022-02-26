def solution(name):
    answer = 0
    shift = len(name) - 1
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) #알파벳 선택

        if(char == 'A'): #이동
            target = i
            while(target<len(name) and name[target] == 'A'):
                target += 1
            if (i == 0):
                left = 0
            else:
                left = i-1
            
            right = len(name) - target
            shift = min(shift, left+right+min(left, right))
            
    answer += shift
    return answer