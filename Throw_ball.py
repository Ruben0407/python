def solution(numbers, k):
    answer = 0

# for문에서 옆자리를 뛰어넘고 카운트



    number = numbers * k
    for i in range(len(number)):
        if i % 2 == 0:
            k -= 1
            if k == 0:
                print(number[i])

solution([1, 2, 3], 3)
