# 1 exercise

class MyClass:
  x = 5

# 2 exercise: Create an object of MyClass called p1:

class MyClass:
  x = 5
p1 = MyClass()


# 3 exercise: Use the p1 object to print the value of x:

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

# 4 exercise: What is the correct syntax to assign a "init" function to a class?

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# 1 exam

class MyClass:
  x = 5

# 2 exam

p1 = MyClass()
print(p1.x)

# 3 exam

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# 4 exam

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

# 5 exam

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# 6 exam

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# 7 exam

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# 8 exam

p1.age = 40

del p1.age

del p1