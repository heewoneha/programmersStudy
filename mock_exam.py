def solution(answers):
    answer = []
    
    one = [1, 2, 3, 4, 5]
    one_count = 0
    
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    two_count = 0
    
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    three_count = 0
    
    for i in range(0, len(answers)):
        if (one[i % len(one)] == answers[i]):
            one_count += 1
        if (two[i % len(two)] == answers[i]):
            two_count += 1
        if (three[i % len(three)] == answers[i]):
            three_count += 1
    
    maximum = max(one_count, two_count, three_count)
    
    if maximum == one_count:
        answer.append(1)
    if maximum == two_count:
        answer.append(2)
    if maximum == three_count:
        answer.append(3)
        
    return answer