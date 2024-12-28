# JSON in Python

## Convert Dictionary to JSON

```python
import json

dict = {
    "name": "Dibya",
    "age": 20,
    "address": "talcher"
}

value = json.dumps(dict)
print(type(value))  # Output: <class 'str'>
```

## Convert JSON String to Python Dictionary

```python
import json

# Fixed the missing closing quote in the JSON string
x = '{"name":"dibya","age":30,"address":"odisha"}'

y = json.loads(x)
print(y)  # Output: {'name': 'dibya', 'age': 30, 'address': 'odisha'}
```

# Classes in Python

## Example: Animal Class

```python
class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def printValue(self):
        print(self.type, self.name)

animal1 = Animal("domestic", "dog")
animal2 = Animal("jungly", "sher")
animal1.printValue()  # Output: domestic dog
```

## Example: Person Class

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("john", 18)
print(person1.name, person1.age)  # Output: john 18
```

## Example: Simple Class with Attribute

```python
class myClass:
    x = 5

p1 = myClass()
print(p1.x)  # Output: 5
```
