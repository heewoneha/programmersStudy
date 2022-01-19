def solution(people, limit):
    answer = 0
    
    people.sort()
    
    i=0
    j = len(people) - 1
    
    while(i <= j): #==포함 이유: i==j인 그 자체 값 하나만 빼기
        answer += 1
        if ((people[i] + people[j]) <= limit):
            i += 1 #pop
        j -= 1 #len
    
    return answer