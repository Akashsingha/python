# f = open('hello.txt')
# d = f.read()

# print(f.tell())

# print(f.name)
# # print(f.closed)

with open('hello.txt', 'r') as f:
    with open('New_file', 'w') as i:
        for s in f.read().replace(",","'"):
            i.write(s)
            if s == "'":
                i.write('s salary is ')
            


