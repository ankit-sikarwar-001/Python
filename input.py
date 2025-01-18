#The input() function in Python is used to accept input from the user via the console. It always returns the input as a string, regardless of what the user types. You can convert this input to other types if necessary. 

#without parameter 
# data  =  input()
# print(f"you entered {data}")

# #with  parameter 
# data = input("enter a value :")
# print(f"you entered {data}")

#with typecasting
# age = int(input("Enter your age : "))
# print(f"Your age : {age}")

#with split
array = input("enter a list of element with space : ").split()
print(f"you entered : {array}")
array.append(50)
array = [arr for arr in array]
print(f"you entered : {array}")

#with condition
while True:
    age = input("Enter your age : ")
    if(age.isdigit()):
        break
    print("Enter integer value ")
print("Your age = ",age)
    