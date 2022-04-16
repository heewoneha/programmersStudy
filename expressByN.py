def solution(N, number): #N으로 표현(동적계획법)
    sets = [set() for x in range(8)]
    for i, x in enumerate(sets, start=1):
        x.add(int(str(N)*i))

    for i in range(0, len(sets)):
        for j in range(0, i):
            for op1 in sets[j]:
                for op2 in sets[i-j-1]:
                    sets[i].add(op1+op2)
                    sets[i].add(op1-op2)
                    sets[i].add(op1*op2)
                    if op2 != 0: #0 divide 방지
                        sets[i].add(op1 // op2)
        if number in sets[i]:
            answer = i+1
            break
        else: #최솟값이 8보다 크면
            answer = -1

    return answer