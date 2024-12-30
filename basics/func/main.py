# ++++ function++++++++

# ++++++ Square of a number +++++++
# def sqaure_of_num(num):
#     return num**2
# value=sqaure_of_num(4)
# print(value)


# ++++++++++++  function with multiple parameters ++++
# def sum_of_two_num(num1,num2):
#     return num1+num2

# print(sum_of_two_num(2,4))

# ++++++++ Polymorphism in Functions ++++++
# def multiply(p1,p2):
#     return p1 * p2

# print(multiply(2,5))
# print(multiply('h',5))

# +++++++++ circle stats +++++++
# import math

# def circle_stats(radius):
#     print("hi")
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius  # Fixed the typo here
#     return round(area,1), round(circumference,1)
    
# a,c=circle_stats(2)
# print("area: ",a,"circumfernece: ",c)


# +++++++ greet someone++++++++++
# def greet(name = "User"):
#     return "Hello, "+name+" !"
# print(greet())




# ++++++++++++lambda func ++++++++++

# cube = lambda x: x ** 3

# greet= lambda name="User":f"Hello , {name}"

# print(cube(3))
# print(greet())




# ++++++++++ function with *args ++++++++
# def sum_all(*chai):
#     print(chai)
#     for i in chai:
#         print(i)
#     return sum(chai)

# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))



# ++++++++ function with *kwargs +++++++
# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# print_kwargs(name="shaktiman",power="lazer",enemy="Dr. Jackaal")

def even_generator(limit):
    for i in range(2,limit+1,2):
        print(i)



















