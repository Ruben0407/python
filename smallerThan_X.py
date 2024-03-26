def count(x):
    n = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]

    answer = []
    # print(n)
    for i in range(len(n)):
        if 0 < n[i] < x:
            answer.append(n[i])
    print(* answer)                
count(5)