#ASK Form 3 PG 210
import math

#First Method
#def kiraPow(x,y):
#   return x ** y


#Second Method
def kiraPow(x,y):
    for i in range (1,y):
        x *= y
    return x


a = pow(2,8)
print(a)