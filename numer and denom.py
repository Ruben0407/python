# 문제풀이 순서
# 분모끼리 곱해서 공약수 찾기
# 분자는 분모의 곱


def solution(numer1, denom1, numer2, denom2):
    d_values = 0
    answer = []

    a = denom1 * denom2
    b = numer1 * denom2
    c = numer2 * denom1
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            d = a // i
            print(d)
            if (b + c) % d == 0:
                answer.append((b + c) // d)
                answer.append(a // d)
            
                print(answer)
            else:
                answer.append(b + c)
                answer.append(a)
                answer.pop(0)
                answer.pop(-1)
                print(answer)
solution(9,2,1,3)


