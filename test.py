def find_gcd(x, y):
        while(y):
            x, y = y, x % y
            print(x)
            
find_gcd(10, 8)

#1 2 3 4 