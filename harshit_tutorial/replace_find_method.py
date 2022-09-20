string = "He play football in the ground and he is also good in sports"
# print(string.replace("in","have",1))

# center method 
string = "Akash" #length of string is 5 adding 4 star = 9
print(string.center(66,"*"))

# Ask user name and add 4 star in front and back

name = input("Enter your name: ")
l = len(name)
print(name.center(l+8,"*"))