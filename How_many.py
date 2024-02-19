def solution(array):
    answer = 0
    count = 0
    for i in range(len(array)):
        for z in range(1001):
            if array[i] == array[z]:
                
                answer += 1
    print(answer)
solution([1, 2, 3, 3, 3, 4])