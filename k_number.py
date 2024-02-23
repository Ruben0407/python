def solution(array, commands):
    answer = []
    answers = []
    for i in range(len(commands)):
        answers = array[commands[i][0] - 1: commands[i][1]]
        answers.sort()
        answer.append(answers[commands[i][2] -1: commands[i][2]])
        flat_list = sum(answer, [])## 지피티
        print(flat_list)

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
