def is_prime(num):
    if(num<=1):
        return False
    if(num == 2):
        return True
    if(num%2 == 0 ):
        return False
    rng =int(num**0.5)
    for i in range(3,rng,2):
        if(num%i == 0):
            return False
    return True

def firstNprime(n):
    primes=[]
    num = 2
    while len(primes) <n:
        if(is_prime(num)):
            primes.append(num)
        num += 1
    return primes

num = 10
primes= firstNprime(num)
print(f"first {num} prime numbers : {primes}")