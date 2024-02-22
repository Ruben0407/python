# def solution(array):
#     answer = 0
#     count = 0
#     for i in range(len(array)):
#         for z in range(1001):
#             if array[i] == array[z]:
                
#                 answer += 1
#     print(answer)
# solution([1, 2, 3, 3, 3, 4])

# def solution(array):
#     answer = 0
#     for i, answers in enumerate(array):
#         # print(i, answers)
#         for z in range(1000):
#             if answers == z:
#                 answer += 1
#                 print(answer)
# solution([1, 2, 3, 3, 3, 4])


# def solution(array):
#     answer = 0
#     answers = []
#     count = 0
#     for z in range(1000):
#         for i, answer in enumerate(array):
#             if z == answer:
#                 count += 1
#                 answers.append(answer)
                
#                 print(count)
# solution([1, 2, 3, 3, 3, 4])


# def solution(array):
#     answer = 0
#     for i in array:
#         print(i)

# solution([1, 2, 3, 3, 3, 4])

def solution(array):

    nlist = [0 for i in range(100)]
    for i in range(len(array)):
        print(array)
        nlist[list[i]] += 1

        print(nlist.index(max(nlist)+ 1))
solution([1, 2, 3, 3, 3, 4])
