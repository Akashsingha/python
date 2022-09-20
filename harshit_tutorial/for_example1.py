# sum of 1 to 10
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n):
    # sum += i
# print(sum)

# num = input("Enter a number: ")
# sum = 0
# for i in range(0,len(num)):
#     sum += int(num[i])
# print(sum)

name = input("Enter a name: ")
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(name[i]," : ",name.count(name[i]))
    temp += name[i]