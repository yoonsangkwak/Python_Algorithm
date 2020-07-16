# 불린 (Boolean)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print("--------------------")

print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("--------------------")

print(not True)
print(not False)
print("--------------------")

print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(3 <= 3)
print(2 == 2)
print(2 != 2)


print("Hello" == "Hello")
print("Hello" != "Hello")
print()

print(2 > 1 and "Hello" == "Hello") # True and True
print("--------------------")

print(not not True) # not False
print(not not False) # not True
print("--------------------")

print(7 == 7 or (4 < 3 and 12 > 10)) # True or False
print("--------------------")

x = 3
print(x > 4 or not (x < 2 or x == 3)) # False or False