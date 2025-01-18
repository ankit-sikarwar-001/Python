def gcd(first, second):
    while second != 0:
        # temp = second
        first,second = second,first % second
        # first = temp
    return first

num1 = 27
num2 = 18
result = gcd(num1, num2)
print("GCD of Two numbers : ", result)