# enter user name at show how nuch time a letter was their
name = input("Enter a name: ")
i = 0
l = 0
temp_var = ""
while i<len(name):
    if name[i] not in temp_var:
        l = name.count(name[i])
        print(name[i],":",l)
        temp_var += name[i]
    else:
        break
    i+=1