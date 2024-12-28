# +++++ function ++++






# def add(num1,num2):
#     print(num1+num2)

# add(3,4)

# def say_hello():
#     print("Hello from dibya")
    
# say_hello()
    


















# ++++++++++ dictionaries +++++++++++
# its is mor ejson in javascript
# +++ nested dict +++++++
# myFamily={
#     "child1":{
#         "name":"dibya",
#         "age":"19"
#     },
#     "child2":{
#         "name":"lokesh",
#         "age":"20"
#     },
#     "child3":{
#         "name":"rashmi",
#         "age":"21"
#     },
# }
# print(myFamily)

# thisdict={
#     "name":"Dibya",
#     "age":23,
#     "model":"altroz"
# }

# thisdict["model"]="verena"
# thisdict["color"]="red"
# for item in thisdict:
#     print(item)
# print(thisdict)










# ++++++++ sets +++++++++++

# myste={"apple","banana","cherry","cherry","apple"}
# myst2={
#     "1",2,"3","4",False
# }
# print(myste)
# print(len(myste))
# for item in myste:
#     print(item)

# total=myste.union(myst2)

# print(total)

# +++++++++++++ tuples ++++++++++++++

# mytuple=("apple","orange","banana","cherrry")
# print(len(mytuple))
# print(mytuple)

# smallTuple=("apple",)
# print(type(smallTuple))

# bigTuple=("false",False,1,"rama",1.04)

# for item in range(len(bigTuple)):
#     print(bigTuple[item])
# print(len(bigTuple))
# print(bigTuple[2])


# list=["False",False,1,2,"DIBya"]
# print(list)











# +++++ list +++++++++


# newlist.append("mixveg")
# newlist.insert(2,"mixveg")
# newlist.remove("orange")


# ++++ looping thorugh lists ++++

# for item in newlist:
#     print(item)




#  +++++++++++++ looping thorugh index numbers ++++++++
# newlist=["banana","orange","apple","cherrry"]
# newlist.sort()
# for item in range(len(newlist)):
#     print(newlist[item])
     
# print(newlist)




# print(newlist)
# print(len(newlist))


# ps: lis items are ordered , changable, allow duplicate value





# +++++++ Boolean ++++++++++

# num1 = 54
# num2 = 67

# if(num1>=num2):
#     print("b is greater than a")
# else:
#     print("a is greater than b")



# print(10>9)
# print(10==9)
# print(10==10)
# print(10<9)


# ++++++++++++++ strings +++++++++

# ++++ f strings +++++

# age = 24
# stmnt=f"my age is like {age}"
# print(stmnt)


# +++++ string concatination ++++
# str="Hello world"
# txt="babsyyyyy"

# print(str+txt)





# a= " So , DIBYA is a great banda yaar"
# print(a.replace("DIBYA","yash"))
# print(a.strip().upper())





# a="hello world"
# print(a.upper())

# a= "DOBY raqswss"
# print(a.lower())




# ++++ slicing +++++ 
# str="heloo world"
# print(str[:5])




# str=" heyyyy you gus are something diff , i never make such kinda good friends"
# if "guys" not in str:
#     print("it is not present in the string")




# txt="the best things in life are free"
# print("expensive"  in txt)




# str ="The best things in life are free"
# print("things" in str)

# for item in str:
#     print(item)
# print(len(str))


# str="what's up! universe"
# print(len(str))





# looping thorugh strings
# str= "banana"
# for item in str:
#   print(item)


# print("he is called johny")
# for multilne strings 
# a =""" lorem dipusm diufeuf iohuh, iho ihuhfue ,bugueigf ,oifhehfuefgfuegfu .wjbu"""
# print(a)

















# ++++++++++ typecasting ++++++++++

# x = 43
# y = 3.4
# z = "73"

# print("before casting ",type(x))
# x = float(43)
# print("after casting the value",type(x))

# print("before casting the value ",type(y))
# y=int(y)
# print("after casting the value",type(y))


# print("before casting the value ",type(z))
# z=int(z)
# print("after casting the value",type(z))




# ++++++++++++++++ using random +++++++++++++++++

# import random
# value = random.randrange(1,10)
# print(value)

# +++++++++++++ checking the type +++++++++++++++++++++++

# x = 35e3
# y = 12E4
# z = -87.7e100

# print(type(x))
# print(type(y))
# print(type(z))