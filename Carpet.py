def solution(brown, yellow):
    answer = []
    
    sum_all = brown + yellow

    for i in range(3, sum_all + 1):
        j = (sum_all // i)
        
        if (i >= j):
            tmp_yellow = (i - 2) * (j - 2)
            if (tmp_yellow == yellow):
                if (brown == (i * 2 + j * 2 - 4)):
                    answer = [i, j]
                    break
    
    return answer