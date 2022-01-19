def solution(price, money, count):
    all_price = 0
    while count > 0:
        tmp = price * count
        all_price += tmp
        count -= 1
    
    if all_price < money:
        answer = 0
    else:
        answer = all_price - money
    
    return answer