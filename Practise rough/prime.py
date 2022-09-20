"""
a = int(input("Enter a number"))

for i in range(2,a):
  if a % i == 0:
     print("Not prime")
     break
else:
    print("Prime")"""

a = int(input("Enter a number: "))

if a% 2 == 0:
    print("Even")
else:
    print("Odd")
