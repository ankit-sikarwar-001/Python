def fibo(num):
    if(num<1):
        return None
    series = [0,1]
    while len(series)<num:
        series.append(series[-1]+series[-2])
    return series[:num]

num = 10
print(f"Fibonacci series upto {num} = {fibo(num)}")