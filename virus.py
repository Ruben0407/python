def solution(n, t):
    answer = 0
    for i in range(1, t + 1):
        n = n * 2
        anwer = n ** 2 + n
        
        print(n)
solution(2, 10)