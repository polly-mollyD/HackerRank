for _ in range(3):
    print("Hello world!")




# the second exercise

l1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
l2 = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth']
for i in range(len(l1)):
    print(l2[i], " prime number is ", l1[i])





# the third exercise

from random import seed
from random import randint

seed(1)

list = []
for i in range(10):
    list.append(randint(0, 100))
    print(list[i],'-', list[i]**2)




# the fourth exercise


from random import seed
from random import randint

seed(1)

sum = 0
list = []
for i in range(10):
    list.append(randint(0, 100))
    sum += list[i]
print(sum)




# the fifth exercise



A = int(input('Please, write down the first integer '))
B = int(input('Please, write down the second integer '))
sum = 0
for i in range(A, B + 1):
     sum += i
print(sum)

# the sixth exercise

la = [1, 2, 4, 5, 6, 7, 8, 9]

lb = la.copy()
print(la)
print(lb)





# the seventh exercise

import turtle

wn = turtle.Screen()
myLittleTurtle = turtle.Turtle()

for i in range(3):
    myLittleTurtle.forward(100)
    myLittleTurtle.left(90)

    myLittleTurtle.forward(100)
    myLittleTurtle.left(90)

    myLittleTurtle.forward(100)
    myLittleTurtle.left(90)

    myLittleTurtle.forward(100)
    myLittleTurtle.left(90)

wn.exitonclick()



# the eighth exercise


import turtle     # this code will work separately

wn = turtle.Screen()
t = turtle.Turtle()

a = int(input('Please, enter the number of sides of the polygon : '))
for i in range(a):
    turtle.forward(100)
    turtle.right(360 / a)


wn.exitonclick()