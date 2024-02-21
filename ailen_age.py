# def solution(age):
#     answer = ''
#     alphabet = ("abcdefghijklmnopqrstuavwxyz")
    
#     for i, answer in enumerate(alphabet):
#         print(f'{answer} = {i}')
    
#     # for i in  range(len(alphabet)):
#     #     for z in range(1000):
#     #         alphabet[i] = z
#             # print()

# def solution(index):
#     alphabet = "abcdefghijklmnopqrstuavwxyz"
#     if index < len(alphabet):
#         print(alphabet[:index + 1])
#     else:
#         print("인덱스가 알파벳 문자열의 길이를 초과합니다.")




# solution(23)
age = 23
answer = ''
list = ["a","b","c","d","e","f","g"]


for i in str(age):
    print(type(age))
    answer += list[int(i)]