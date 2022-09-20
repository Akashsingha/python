
age = int(input("Enter your age: "))
if age<=3:
    print("Ticket is free")
elif age>=4 and age<=10:
    print("Ticket price is 150/-")
elif age>=11 and age<=60:
    print("Ticket price is 250/-")
else:
    print("Ticket price is 200/-")