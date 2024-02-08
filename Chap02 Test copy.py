def sample(n):
    if n == 0:
        return
    print(n)
    n -= 1
    sample(n)
    
sample(10)
