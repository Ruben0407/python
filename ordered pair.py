#  -- 공약수 구하기 문제
#     1.for문
#     2.if 문 n % i == 0:
        
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += 1
            print(answer)
solution(20)