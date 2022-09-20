#  input a name and a character and check how much time it is count 
name ,char = input("Enter name and charcter with comma separated").split(",")
print(name.lower().count(char.lower()))
# "  Akash   "-----> "Akash" -------> "akash"
# " A   "----> "A" ------> "a"
print(name.replace(" ","").lower().count(char.replace(" ","").lower()))