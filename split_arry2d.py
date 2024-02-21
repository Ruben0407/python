def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        # i = 0 2 4 6
        answer.append(num_list[i: i + n])
        print(answer)
                                                                                                                                                                   


solution([1, 2, 3, 4, 5, 6, 7, 8], 2)

