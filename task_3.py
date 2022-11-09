def is_prime(n):
    prime = True
    if n <= 1:
        prime = False
    elif n == 2:
        prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    return True

def is_diabolic(n):
    if "666" in str(n):
        return True
    else:
        return False
result = 0
for i in range(1,100001):
    if is_prime(i) is True and is_diabolic(str(i)) is True:
        result += 1
        print(i)
print(f"ilosc {result}")


