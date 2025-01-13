# Python print() function prints the message to the screen or any other standard output device. In this article, we will cover about print() function in Python as well as it’s various operations.

# we can use three types of keywords like sep, end , file 

#using sep 
a= 13
b= "01"
c = 25
print(a,b,c,sep="-")

#using end
a= 13
b= "01"
c = 25

print(a,b,c,sep="-",end =";")

#using file 
a= 13
b= "01"
c = 25
print(a,b,c,sep="-",file= open("file.txt","a"))

#format method one 
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age))

#format method two
name = "Ankit"
age = 22
print(f"Name: {name}, Age: {age}")

#format method third
name = "Piyush"
age = 21
print("Name: %s, Age: %d"%(name,age))
