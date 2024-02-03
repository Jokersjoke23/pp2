# 1 exercise: What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?

#(class Student(Person):)

# 2 exercise: We have used the Student class to create an object named x.
# What is the correct syntax to execute the printname method of the object x?

class Person:
  def __init__(self, fname):
    self.firstname = fname
    
  def printname(self):
    print(self.firstname)
    
class Student(Person):
  pass

x = Student("Mike")
x.printname()

# 1 exam

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# 2 exam

x = Student("Mike", "Olsen")
x.printname()

# 3 exam

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

# 4 exam

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# 5 exam

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# 6 exam

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

# 7 exam

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# 8 exam

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)