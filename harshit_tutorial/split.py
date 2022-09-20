# from ntpath import join


# user_info = "harshit 23".split()
# # print(user_info)
# l = ['sh','khi']
# print(''.join(l))

# Define a function that take two arguments 
l = ["Akash","singha","erv","abc"]
def find(l,s):
    for i ,name in enumerate(l):
        if name == s:
            return i
    else:
        return -1
print(find(l,"Akash"))