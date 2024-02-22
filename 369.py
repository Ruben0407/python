# def solution(order):
#     answer = 0
#     new_order = []
#     new_order.append(order)
#     for i in enumerate(order):
#         print(i)
#         new_order.append(order)
### 지피티 도움을 받음
def solution(order):
    answer = 0
    cnt = 0
    list_a = [int(i) for i in str(order)]##여기
    for z in range(len(list_a)):
        if list_a[z] % 3 == 0 and list_a[z] != 0:
            cnt += 1
            
            print(cnt)
solution(3)