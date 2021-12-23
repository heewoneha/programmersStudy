def solution(participant, completion):
    dic = {}

    for person in participant:
        if person not in dic:
            dic[person] = 1
        else:
            dic[person] += 1
    
    for who in list(dic.keys()):
        if who not in completion:
            return who
    
    for who in completion:
        if dic.get(who) != completion.count(who) :
            return who