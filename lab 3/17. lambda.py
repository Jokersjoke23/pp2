# 1 exercise

x = lambda a : a

# 1 exam

x = lambda a : a + 10
print(x(5))

# 2 exam

x = lambda a, b : a * b
print(x(5, 6))

# 3 exam

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# 4 exam

def myfunc(n):
  return lambda a : a * n

# 5 exam

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# 6 exam

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

# 7 exam

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))