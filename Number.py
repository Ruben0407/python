arr = [1,2,3]
a = len(arr)
for i in range(a):
    a = arr.pop()
      
answer = a * a
answer.append(a)

print(answer)
 