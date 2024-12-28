# +++++++++ json in python ++++++++
# +++++conver dict to python +++
import json
dict={
    "name":"Dibya",
    "age":20,
    "address":"talcher"
}
value = json.dumps(dict)
print(value)
print(type(value))



# import json

# # Fixed the missing closing quote in the JSON string
# x = '{"name":"dibya","age":30,"address":"odisha"}'

# y=json.loads(x)
# print(y)


# class Animal:
#     def __init__(self,type,name):
#         self.type=type
#         self.name=name
#     def printValue(self):
#         print(self.type,self.name)

# animal1=Animal("domestic","dog")
# animal2=Animal("jungly","sher")
# animal1.printValue()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# person1=Person("john",18)
# print(person1.name, person1.age)

# class myClass:
#     x = 5

# Fixed indentation to make this functional and corrected spelling errors in comments
# p1 = myClass()
# print(p1.x)
