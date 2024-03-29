from itertools import combinations

def solution(m, weights):
    answer = 0

    for i in range(len(weights)):
        comb = combinations(weights, i)
        answer += [sum(weight) for weight in comb].count(m)
    
    return answer