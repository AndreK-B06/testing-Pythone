print("hello world")

# Comment test
x = 2
y = 8
"""
Comment test
with multiple lines.
"""
a = str(1 + 3)
b = int(1 + 3)
c = float(1 + 3)
d = 3
e = "Tor"
A = 'Tor'

print(a)
print(b)
print(c)
print(A)

print(type(d))
print(type(e))

userFirstName = "Arne"
print(userFirstName)

X, Y, Z = "Blue", "Read", "Black"

print(X)
print(Y)
print(Z)

names = ["Kai", "Andrine", "Per"]

B, C, D = names

print(B)
print(C)
print(D)
print(b,d,e)

def userName():
    print("Tor is:" + " " + a + " " + "Yeas old")

userName()

import random

print(random.randrange(1, 100))

user1561FullName = str("John" + "" + "pedersen")

print(user1561FullName[4:7])

text = ("I howe \"you\" hav a nice day")
print(text)

age1 = 97
age2 = 16
yes = "welcome"
no = "You are to young"

#  IF ELSE
if age1 > age2:
    print(yes)

else:
    print(no)
    
# List
shoppingList = ["Banana", "Pizza", "Apple", "Soda", "Salad", "Burger"]
shoppingListNextDay = ["Caff", "Tee", "Cake"]
print(shoppingList)
print(len(shoppingList))
print(type(shoppingList))
shoppingList.append("Orange")
print(shoppingList)
shoppingList.extend(shoppingListNextDay)
print(shoppingList)