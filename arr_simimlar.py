def solution(s1, s2):
    sum_len = len(s1) + len(s2)
    answer = 0
    for i in range(len(s1)):
        for z in range(len(s2)):
            if s1[i] == s2[z]:
                answer += 1
                
            else:
                answer = 0
        print(answer)
solution(["a", "b", "c"], ["com", "b", "d", "p", "c"])