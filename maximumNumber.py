def solution(numbers):
    answer = ''

    ch = [str(x) for x in numbers]
    ch.sort(key = lambda x: x*3)
    ch.reverse()

    if ch[0] == '0':
        return '0'

    for c in ch:
        answer += c

    return answer