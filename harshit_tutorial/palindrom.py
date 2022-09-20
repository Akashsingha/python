

# def palindrom(name):
#     new_name = ""
#     for i in range(0,len(name)):
#         new_name += name[(len(name)-1)-i]
#     if new_name == name:
#         return "palindrom"
#     return "Not palindrom"

# name = input("Enter a name: ")
# print(palindrom(name))


def palindrom(name):
    new_name = name[::-1]
    if new_name == name:
        return "palindrom"
    return "Not palindrom"

name = input("Enter a name: ")
print(palindrom(name))