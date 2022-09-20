# class Person:
#     def __init__(self,first_name,last_name,age):
#         print("Hello world")
#         self.first_name = first_name
#         self.last_name = last_name
#         self.number = age

# p1 = Person("Akash","Singha",17)

# print(p1.number)

# Create a laptop class with attributes like brand name, model name, price
# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.name = brand_name
#         self.model = model_name
#         self.price = price


# l1 = Laptop("Acer","HIL56",45000)
# l2 = Laptop("HP","KCB750",50000)
l = [1,2,3]
# l.clear()
# list.clear(l)
# l.append(10)
# list.append(l,10)
# print(l)

# Create a laptop class with attributes like brand name, model name, price
class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.name = brand_name
        self.model = model_name
        self.price = price

    def apply_discount(self, discount):
        # 40%   40/100*50000
        return  self.price - ((discount/100)*self.price)

l1 = Laptop("Acer","HIL56",45000)
l2 = Laptop("HP","KCB750",63000)

print(l2.apply_discount(5))