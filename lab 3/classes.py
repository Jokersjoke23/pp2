# 1 class

class twoMethods:
    def __init__(self):
        self.input = ""
    def getString(self):
        self.input = input("Введите строку: ")
    def printString(self):
        self.input = print("Результат:", self.input.upper())
a = twoMethods()
a.getString()
a.printString()


# 2 class

class Shape:
    def __init__(self):
        self.area = 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def getLength(self):
        self.length = int(input("Type length:"))

    def calculateArea(self):
        self.area = self.length * self.length
        return self.area
a = Square(0)
a.getLength()
print("Area is equal", a.calculateArea())


# 3 class

class Shape:
    def __init__(self):
        self.area = 0

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def getParameters(self):
        self.width = int(input("Vvedite wirinu: "))
        self.length = int(input("Vvedite dlinu: "))

    def printArea(self):
        self.area = self.width * self.length
        return self.area

a = Rectangle(0,0)
a.getParameters()
print("Area of this Rectangle is equals:", a.printArea())


# 4 class

from math import sqrt
class Point:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def getData(self):
        self.x1 = int(input("x1: "))
        self.y1 = int(input("y1: "))
        self.x2 = int(input("y2: "))
        self.y2 = int(input("x2: "))

    def showCoordinates(self):
        return self.x1, self.y2, self.x2, self.y2
    
    def changeCoordinates(self):
        self.x1 = int(input("x1: "))
        self.y1 = int(input("y1: "))
        self.x2 = int(input("y2: "))
        self.y2 = int(input("x2: "))
    
    def distCoordinates(self):
        return sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

a = Point()
a.getData()
print("Coordiantes: {}".format(a.showCoordinates()))
a.changeCoordinates()
print("New coordinates {}".format(a.showCoordinates()))
print("Distation: {}".format(a.distCoordinates()))


# 5 class

class bankAccount:
    def __init__(self, owner = "", balance = 0):
        self.balance = balance
        self.owner = owner

    def deposit(self):
        aqshaqosu = int(input("Сумма депозита: "))
        self.balance += aqshaqosu
        print("Успешно!")
        print(f"Ваш текущий баланс(тг): {self.balance}")
    
    def withdraww(self):
        withdraw = int(input("Сумма вывода: "))
        if withdraw > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= withdraw
            print("Успешно!")
            print(f"Ваш текущий баланс: {self.balance}")

bankOperation = bankAccount(input("ФИО:"), int(input("Введите ваш баланс: ")))
while True:
    typeoper = input("Введите тип операции (Withdraw/Deposit/Exit): ")
    if typeoper == "Withdraw":
        bankOperation.withdraww()
    elif typeoper == "Deposit":
        bankOperation.deposit()
    elif typeoper == "Exit":
        break
    else:
        print("Неправильный ввод операции.")


# 6 class

a = list(map(int, input().split()))
print(list(filter(lambda x: all(map(lambda s: x % s, range(2, x))), a)))