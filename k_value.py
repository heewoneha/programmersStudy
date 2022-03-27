def solution(array, commands): #K번째수 (정렬)
    answer = []
    
    for i in range(0, len(commands)):
        what = commands[i]

        arr = []

        x = commands[i][0] - 1
        y = commands[i][1] - 1
        for a in range(x, y + 1):
            arr.append(array[a])
        
        arr.sort()
        
        x = commands[i][2] - 1
        answer.append(arr[x])
    
    return answer

solution([1,5,2,6,3,7,4], [[2,5,3],[4,4,1],[1,7,3]])