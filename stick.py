def solution(n, k):
    answer = 0
    stick = 12000
    juice = 2000
    for i in range(n):
        if n // 10 == 1 * i:
            k -= 1 * i
            answer = (stick * n) + (juice * k)
            print(answer)
solution(10, 3)
