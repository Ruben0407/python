n = 10 #피자 한판에 6조각 * n
answer = 0
pizza = 6

for i in range(1, 101):
    if pizza % i == 0 and n % i == 0:
        a = (pizza // i) * (n // i) * i
        answer = a // 6
         
        print(answer)
    #for z in range()