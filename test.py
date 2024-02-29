a = [3, 30, 34, 5, 9]	
b = ''.join(map(str, a))
c = []
print(b)
for i in range(len(a)):
    # b = ''.join(map(str, a))
    c.append(b[i])

    # for z in range(len(a)):
        # c.append(b)
print(c)
# print(type(a))