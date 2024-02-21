# 문제풀이 순서
# 분모끼리 곱해서 공약수 찾기
# 분자는 분모의 곱


# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     denom = denom1 * denom2 
#     # 8
#     # 6
#     numer_multiply1 = numer1 * denom2
#     # 4
#     # 27
#     numer_multiply2 = numer2 * denom1
#     # 6
#     # 2
#     for i in range(2, denom + 1):
#         #2 3 4 5 6 7 8 
#         if denom % i == 0 and numer_multiply1 % i == 0 and numer_multiply2 % i == 0:
#             # i = 2
#             answer.append((numer_multiply1 + numer_multiply2) // i)
#             answer.append(denom // i)
#             print(answer)
#             # [5, 4]
#         elif denom % i == 0 and numer_multiply1 % i != 0 and numer_multiply2 % i == 0:
#             # i = 2 3 6
#             answer.append(numer_multiply1 + numer_multiply2)
#             answer.append(denom)
#             print(answer)
        

# # solution(1,2,3,4)
# # solution(9,2,1,3)
# solution(3,4,2,7)

###### gpt가 풀어줌 ####
def solution(numer1, denom1, numer2, denom2):
    # 분모끼리 곱하기
    denom = denom1 * denom2 

    # 분자는 분모의 곱으로 나누기
    numer = numer1 * denom2 + numer2 * denom1

    # 최대공약수 찾기
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    gcd = find_gcd(numer, denom)

    # 분자와 분모를 최대공약수로 나누기
    answer = [numer // gcd, denom // gcd]

    return answer
print(solution(9,2,1,3))