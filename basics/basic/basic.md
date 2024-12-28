# Python Basics Notes

## Type Casting

```python
x = 43
y = 3.4
z = "73"

print("before casting ", type(x))
x = float(43)
print("after casting the value", type(x))

y = int(y)
print("after casting the value", type(y))

z = int(z)
print("after casting the value", type(z))
```

---

## Random Module

```python
import random
value = random.randrange(1, 10)
print(value)
```

---

## Checking Types

```python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

---

## Strings

### F-Strings

```python
age = 24
stmnt = f"my age is like {age}"
print(stmnt)
```

### String Concatenation

```python
str = "Hello world"
txt = "babsyyyyy"
print(str + txt)
```

### String Methods

```python
a = " So , DIBYA is a great banda yaar"
print(a.replace("DIBYA", "yash"))
print(a.strip().upper())

b = "hello world"
print(b.upper())
print(b.lower())
```

### Slicing Strings

```python
str = "heloo world"
print(str[:5])
```

### String Checks

```python
str = " heyyyy you gus are something diff , i never make such kinda good friends"
if "guys" not in str:
    print("it is not present in the string")

txt = "the best things in life are free"
print("expensive" in txt)

str = "The best things in life are free"
print("things" in str)

for item in str:
    print(item)

print(len(str))
```

---

## Boolean

```python
num1 = 54
num2 = 67

if num1 >= num2:
    print("b is greater than a")
else:
    print("a is greater than b")

print(10 > 9)
print(10 == 9)
print(10 == 10)
print(10 < 9)
```

---

## Lists

Lists are ordered, changeable, and allow duplicate values.

```python
newlist = ["banana", "orange", "apple", "cherry"]
newlist.append("mixveg")
newlist.insert(2, "mixveg")
newlist.remove("orange")

newlist.sort()

for item in range(len(newlist)):
    print(newlist[item])

print(newlist)
print(len(newlist))
```

---

## Tuples

Tuples are ordered and immutable collections.

```python
mytuple = ("apple", "orange", "banana", "cherry")
print(len(mytuple))
print(mytuple)

smallTuple = ("apple",)
print(type(smallTuple))

bigTuple = ("false", False, 1, "rama", 1.04)

for item in range(len(bigTuple)):
    print(bigTuple[item])

print(len(bigTuple))
print(bigTuple[2])
```

---

## Sets

Sets are unordered collections of unique elements.

```python
myste = {"apple", "banana", "cherry", "cherry", "apple"}
myst2 = {"1", 2, "3", "4", False}

print(myste)
print(len(myste))

for item in myste:
    print(item)

total = myste.union(myst2)
print(total)
```

---

## Dictionaries

Dictionaries are similar to JSON objects in JavaScript.

### Nested Dictionary Example:

```python
myFamily = {
    "child1": {
        "name": "dibya",
        "age": "19"
    },
    "child2": {
        "name": "lokesh",
        "age": "20"
    },
    "child3": {
        "name": "rashmi",
        "age": "21"
    }
}
print(myFamily)
```

### Updating Dictionary:

```python
thisdict = {
    "name": "Dibya",
    "age": 23,
    "model": "altroz"
}

thisdict["model"] = "verena"
thisdict["color"] = "red"

for item in thisdict:
    print(item)

print(thisdict)
```

---

## Functions

```python
# Function to add two numbers
def add(num1, num2):
    print(num1 + num2)

add(3, 4)

# Function to print a greeting
def say_hello():
    print("Hello from dibya")

say_hello()
```
