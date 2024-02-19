# def solution(array):
a = [1, 2, 3, 3, 3, 4]

#     count = [0] * (max(a) + 1)
#     for i in a:
#         count[i] += 1
#     m = 0
#     for z in count:
#         if z == max(count):
#             m += 1
#     if m > 1:
#         return -1
#     else:
#         return count.index(max(count))
#         print(a)
# solution([1, 2, 3, 3, 3, 4])
    # for answer in enumerate(a):
    #     print(answer)

count = [0] * (max(a) + 1)
count1 = max(a)
count2 = [0] * max(a)
print(count2)