def solution(phone_book): #무조건 맨 앞 번호가 접두어가 아님.
    answer = True
    
    phone_book.sort()
    
    for i in range(0, len(phone_book) - 1):
        if (phone_book[i] == phone_book[i+1][:len(phone_book[i])]):
            answer = False
    
    return answer