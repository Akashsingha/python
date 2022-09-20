#python program to read a number n and compute n+nn+nnn
print("Enter a number n:")
n = int(input())
temp = str(n)
t1 = temp+temp 
t2 = temp+temp+temp
comp = n +int(t1)+int(t2)
print(comp)
