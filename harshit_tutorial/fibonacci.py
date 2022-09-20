# fibonacci series program 
# 0 1 1 2 3 5 8 13 21 34
 
def fibonacci(l):
    a = 0
    b = 1

    for i in range(l):
        if i==0:
            print(a,end = " ")
        if i==1:
            print(b,end = " ")
        c = a+b
        a = b
        b = c
        print(c,end = " ") 

fibonacci(20)