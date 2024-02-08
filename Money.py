while True:
    counter = [500,100,50,10]
    money = 3580
    for i in range(4):
        a = money / counter[i]
        print("받은 동전:", counter[i],":",int(a))

        money %= counter[i]
        print(money)
        
    break
        
        # elif money:
        #     b = money / counter[1]
        #     print("받은 동전:","100원",b)




# if money % counter[0] == 0:
#     a = money / counter[0]
#     money %= counter[0]
#     print("받은 동전:", "500원:",int(a))
#     print("잔돈없다")
# elif money % counter[1] == 0:
#     b = money / counter[1]
#     money %= counter[1]
#     print(int(b))

# elif money % counter[2] == 0:
#     c = money / counter[2]
#     money %= counter[2]
#     print(int(c))
# elif money % counter[2] == 0:
#     d = money / counter[3]
#     money %= counter[3]
#     print(d)
    #print("받은 동전:", "500원:",int(a), "100원:",int(b), "50원:",int(c), "10원:",int(d))