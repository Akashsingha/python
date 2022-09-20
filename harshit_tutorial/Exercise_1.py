# define a function which will take list containing numbers as input 

# def square_list(l):
#     square = []
#     for i in l:
#         square.append(i*i)
#     return square

# numbers = [1,2,3,4]

# print(square_list(numbers))

# define a function which will take list as a arguments and this function will return a list

# def reverse(l):
#     reverse = []
#     for i in range(len(l)):
#         c = l.pop()
#         reverse.append(c)
#     return reverse

# numbers = ["Word1","words2","words3","words4","words5"]
# print(numbers)
# print(reverse(numbers)) 


# define a function that take list of words as argument and return list with reverse of every element in that list 


# def reverese(l):
#     reverse = []
#     for i in range(len(l)):
#         word = words.pop()
#         word = word[::-1]
#         reverse.append(word)
#     return reverse
# def reverese(l):
#     reverse = []
#     for i in l:
#         reverse.append(i[::-1])
#     return reverse

# words = ["abc","tuv",'xyz']
     
# print(reverese(words))

# def odd_even(l):
#     new_list1 = []
#     new_list2 = []

#     for i in l:
#         if (i%2) == 0:
#             new_list1.append(i)
#         else:
#             new_list2.append(i)
#     new_list = [new_list1, new_list2]
#     return new_list

# num = list(range(1,11))

# print(odd_even(num))

# def common_element(l1,l2):
#     l3 = []
#     for i in range(len(l1)):
#         if l1[i] == l2[i]:
#             l3.append(l1[i])

#     return l3

# print(common_element([1,2,5,8],[1,2,7,6]))

# last exercise 
def count_list(l):
    count = 0
    for i in l:
        if type(i) is list:
            count +=1
    return count

print(count_list([1,2,3,4,[23,4,6,4],[2,7,5,43,],[3,89,6,2,1]]))
