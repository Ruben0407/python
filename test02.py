# def solution(numer1, denom1, numer2, denom2):
#     d_values = 0
#     answer = []

#     a = denom1 * denom2
#     b = numer1 * denom2
#     c = numer2 * denom1
#     for i in range(2, a):
#         if (b + c) % i == 0:
#             d = (b + c) // i
#             if d == 0:  # d_values가 아직 0이면 d를 출력하고 d_values를 업데이트
#                 print(d)
# solution(1,2,3,4)


def solution(numer1, denom1, numer2, denom2):
    d_values = 0 

    a = denom1 * denom2
    b = numer1 * denom2
    c = numer2 * denom1
    for i in range(2, a):
        if (b + c) % i == 0:
            d = (b + c) // i
            if d_values == 0:  # d_values가 아직 0이면 d를 출력하고 d_values를 업데이트
                d_values = d
                print(d_values)

solution(1,2,3,4)