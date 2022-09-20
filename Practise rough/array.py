import array
a = array.array('i',[5,4,8,6,12])
print("Elements are: ")
y = a[1:4]

for i in y:
    print(i)
print("Elements are: ")
z = a[0:]

for i in z:
    print(i)


