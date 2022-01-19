import math
from itertools import permutations

def is_prime(num):
    if (num <= 1):
        return False
    
    if (num % 2 == 0): #짝수
        if (num == 2):
            return True
        else:
            return False
    
    i = 3
    while(i <= math.sqrt(num)):#홀수
        if (num % i == 0):
            return False
        i+=2
        
    return True #그 외
        
def solution(numbers):
    answer = 0
    
    numbers = [str(x) for x in numbers]
    tmp = []
    
    for i in range(1, len(numbers) + 1): #가능한 경우 다 확인
        tmp += permutations(numbers, i)
        
    combine = [int(("").join(x)) for x in tmp]
    combine = set(combine) #중복제거
    
    for num in combine: #소수 개수 검사
        if (is_prime(num)):
            answer += 1
    
    return answer