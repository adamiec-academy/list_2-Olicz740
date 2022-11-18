def is_prime(n):
    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
        return prime

def is_diabolic(n):
    if "666" in str(n):
        return True
    else:
        return False

    
result = 0

for i in range(1,100001):
    if is_diabolic(i) and is_prime(i):
        result += 1
        print(i)

print(f"ilosc {result}")
