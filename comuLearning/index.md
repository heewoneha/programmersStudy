# 💻 프로그래머스 커뮤러닝 3기 Python
### 공부하고 기록하는 곳

- [x] 3/22 OT
- [x] 3/23 ~ 3/27 코딩테스트
- [x] 3/28 코드리뷰
> 1. hash()를 새롭게 알게 됐다. 내장함수로, 객체의 해시 값을 돌려준다. 해시 문제에서 요긴하게 사용할 수 있다.
> 2. 내장 모듈인 defaultdict 또한 배웠다. 사용하려면 아래처럼 import 해야한다. 딕셔너리처럼 사용 가능, 기본값 세팅 유용
```python
from collections import defaultdict
dic = defaultdict(int) #0으로 value 값 세팅
```
- [x] 3/29 학습기간 (해시, 그리디, 정렬)
> [체육복(그리디)](https://programmers.co.kr/learn/courses/30/lessons/42862) 문제는 문제 자체에서 30명 제한을 걸어두었지만,
  만약 전체 학생 수만 지나치게 늘렸을 때를 생각해보면 기존에 작성했던
   n번의 탐색은 비효율적이었다. 집합으로 풀면 klogk에 비례하여 더 효율적이다.
   (set(r)의 원소 수를 k라고 하자. s = lost와 reserve의 교집합, l = lost와 s의 차집합,
    r = reserve와 s의 차집합이다. r 집합은 퀵정렬한다.)
- [x] 3/30 ~ 4/3 모의테스트
> 문제 유출 엄금, 기록 X
- [x] 4/4 ~ 4/5 리뷰기간
- [x] 4/6 ~ 4/8 코딩테스트
- [x] 4/11 리뷰기간
- [x] 4/12 학습기간 (힙, 동적계획법, DFS/BFS)
> [N으로 표현](https://programmers.co.kr/learn/courses/30/lessons/42895) 문제에서, 사칙연산을 할 때 +, * 는 교환법칙이 성립하므로, 중복을 없애주기 위해 set을 사용하는 아이디어가 우선 중요하다. 
```python
    for i in range(0, len(sets)): # 코드의 일부분
        for j in range(0, i):
            for op1 in sets[j]: # j == ( 1 길이 ~ N-1 길이 )
                for op2 in sets[i-j-1]: # i-j-1 == ( N-1 길이 ~ 1 길이)
                    sets[i].add(op1+op2)
                    sets[i].add(op1-op2)
                    sets[i].add(op1*op2)
                    if op2 != 0:
                        sets[i].add(op1 // op2)
```
- [x] 4/13 ~ 4/15 최종테스트
> 문제 유출 엄금, 기록 X
- [x] 4/18 ~ 4/19 리뷰기간

<hr/>