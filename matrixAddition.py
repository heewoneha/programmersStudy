def solution(arr1, arr2): #프로그래머스 스킬체크 1, 행렬의 덧셈
    answer = [[]]
    
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    
    return arr1