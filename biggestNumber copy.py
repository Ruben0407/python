def solution(numbers):
    answer = ''
    numbers.sort()
    number = []
    other_number = []
    #[3, 5, 9, 30, 34]
    for i in range(len(numbers)):
        if numbers[i] < 10:
            number = numbers[i]
            # print(number)
        else:
            other_number = numbers[i]
            other_number //= 10
            # print(other_number)
            
    for x in range(len(numbers)):        
        for z in range(x + 1, len(numbers)):
            if numbers[x] < numbers[z]:
                numbers[x], numbers[z] = numbers[z], numbers[x]
                # print(numbers)
                #[34, 30, 9, 5, 3]
solution([3, 30, 34, 5, 9])