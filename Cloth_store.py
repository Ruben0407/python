def solution(price):
    answer = 0
    if 300000 > price >= 100000:
        answer = int(price * 0.95)#0.05를 빼서 구하지말고 바로 구하면 풀이가 완성
    elif 500000 > price >= 300000:
        answer = int(price * 0.9)#마찬가지
    elif price >= 500000:
        answer = int(price * 0.8)
    else:
        answer = price
    print(answer)
    
solution(100010)