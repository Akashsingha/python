# ask user,s name and age 
# if user,s name start with ('a' or 'A') and age is above 10 
# print you can watch coco movie 
# else 'sorry, you can,t watch coco'

n,age = input("Enter your name and age with comma separated: ").split(",")
if (n[0] == 'a' or n[0] == 'A') and (int(age) >=10):
    print("You can watch coco movie")
else:
    print("Sorry,you cannot watch coco")