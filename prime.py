def is_prime(num):
    if(num <= 1 ):
        return False
    if(num == 2 ):
        return True
    if(num%2 == 0 ):
        return False
    rng = int(num**0.5)
    for i in range(3,rng,2):
        if(num % i == 0):
            return False
    return True

num = int(input("Enter a number : "))
if(is_prime(num)):
    print(f"Your entered number {num} is prime ")
else:
    print(f"Your entered number {num} is not prime ")