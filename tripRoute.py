from collections import defaultdict

def solution(tickets):
    answer = []
    v = defaultdict(list)

    def DFS(x):
        while v[x]:
            DFS(v[x].pop(0))
        
        if not v[x]:
            answer.append(x)
            return

    for i, j in tickets:
        v[i].append(j)
    for i, j in v.items():
        v[i].sort()

    DFS('ICN')

    return list(reversed(answer))