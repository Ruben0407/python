def solution(n): #지피티가 도와줌
    answer = 0
    n
    if n <= 0:
        return"1 이상이여야함"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return(b)

print(solution(3))