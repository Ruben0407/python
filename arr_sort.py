def solution(n):
    answer = [[]]
    for i in range(n):
        for z in range(n):
            if len(answer[i]) == 4:
                answer[i].append(z)
                print(answer)
solution(4)