#Python program to print all numbers in a range divisible by a given number.

low = int(input("Enter lower limit"))
upper = int(input("Enter upper limit"))

x = int(input("Enter a number:"))
for i in range(low,upper):
    if(i%x == 0):
        print(i)
