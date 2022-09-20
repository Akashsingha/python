print("Enter a number")
x = int(input())
reverse = 0
while(x!=0):
    reminder = x%10
    reverse = (reverse*10) + reminder
    x = x//10
print(reverse)
