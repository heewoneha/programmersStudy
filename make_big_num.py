def solution(number, k):
    answer = ''
    
    number = [int(x) for x in number]
    
    stack = []
    
    for i in range(0, len(number)):
        c = number[i]
        while(len(stack) > 0 and k > 0 and stack[-1] < c):
            stack.pop(-1)
            k -= 1
        stack.append(c)
    
    while(k > 0):
        stack.pop(-1)
        k -= 1

    for num in stack:
        answer += str(num)
    
    return answer

print(solution("987654321", 8)) #test case 12