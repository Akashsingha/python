def func(num, *args):
    if args:
        return [i**num for i in args]
    else:
        print("You didn't pass any args")
   

print(func(3,*[2,3,4]))