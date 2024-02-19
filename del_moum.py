# def solution(my_string):
#     answer = ''
#     moum = 'aeiou'
#     while my_string not in moum:
#         for i in range(len(moum)):
#             for z in range(len(my_string)):
#                 if moum[i] == my_string[z]:

#                     answer = my_string.replace(moum[i], '')
#                 print(answer)
# solution("nice to meet you")


def solution(my_string):
    moum = ('a,e,i,o,u')
    for i in moum:
        my_string = my_string.replace(i, '')
        print(my_string)
solution("nice to meet you")
