# 문제는 이방향이 아님
def solution(numbers):
    append_str = []
    str_number = ''.join(map(str, numbers))
    
    for i in range(len(str_number)):
        append_str.append(str_number[i])
    for z in range(len(append_str)):
        for x in range(z + 1, len(append_str)):
            if append_str[z] < append_str[x]:
                append_str[z], append_str[x] = append_str[x], append_str[z]
    answer = ''.join(map(str, append_str))
    print(answer)

solution([3, 30, 34, 5, 9])