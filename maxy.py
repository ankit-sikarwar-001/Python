arr = [13,23,43,22,11]
# arr2 = input("Enter a group of numbers with space : ").split()
# arr2= [int(ar) for ar in arr2]
max = arr[0]
for num in arr:
    if(num > max):
        max = num
print(arr , "\n Maximum from the list = ",max)