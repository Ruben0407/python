def solution(emergency):
    answer = []
    # count = []
    # for i in range(len(emergency)):
    #     for z in range(1, len(emergency)):
    #         if emergency[i] < emergency[z]:
    #             for y in enumerate(emergency):
    #                 print()

    #     # print(count)
#     answer =  [sorted(emergency, reverse=True).index(e)+1 for e in emergency]
#     print(answerd)
# solution([3, 76, 24])



def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for i in emergency:
        index = sorted_emergency.index(i) + 1
        answer.append(index)
        print(answer)


solution([3, 76, 24])
