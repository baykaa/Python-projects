# class Point:
#     """ Create a new Point, at coordinates x, y """

#     def __init__(self, x=0, y=0):
#         """ Create a new point at x, y """
#         self.x = x
#         self.y = y
        
#     def __str__(self):    # All we have done is renamed the method
#             return "({0}, {1})".format(self.x, self.y)

# class Rectangle:
#     """ A class to manufacture rectangle objects """

#     def __init__(self, posn, w, h):
#         """ Initialize rectangle at posn, with width w, height h """
#         self.corner = posn
#         self.width = w
#         self.height = h

#     def __str__(self):
#         return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

# box = Rectangle(Point(0, 0), 100, 200)


# bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game for example :D

# print("box: ", box)

# print("bomb: ", bomb)

# print("box before change : ", box)

# box.width += 50

# box.height += 100

# print("box after change : ", box)

# class Fraction:
#      def __init__(self, top, bottom):
#     #The __init__ method to initialize the class, and roughly what represents a co
#          self.num = top # the numerator is on top
#          self.den = bottom # the denominator is on the bottom
#      def __str__(self):
#          return str(self.num) + "/" + str(self.den)
#     #The self parameter refers to the instance of the object
#      def getNum(self):
#          return self.num
#      def getDen(self):
#          return self.den
# myfraction = Fraction(3, 4)
# print(myfraction)
# print(myfraction.getNum())
# print(myfraction.getDen())

# class Fraction:

#     def __init__(self, top, bottom):

#         self.num = top        # the numerator is on top
#         self.den = bottom     # the denominator is on the bottom

#     def __str__(self):
#         return str(self.num) + "/" + str(self.den)


# myfraction = Fraction(3, 4)
# yourfraction = Fraction(3, 4)
# print(myfraction is yourfraction)

# ourfraction = myfraction
# print(myfraction is ourfraction)

# import copy
# p1 = Point(3, 4)

# p2 = copy.copy(p1)

# print(p1 is p2)


# EXERCISE
# A

# class Point:
#     """ Create a new Point, at coordinates x, y """

#     def __init__(self, x=0, y=0):
#         """ Create a new point at x, y """
#         self.x = x
#         self.y = y
        
#     def __str__(self):    # All we have done is renamed the method
#             return "({0}, {1})".format(self.x, self.y)


# class Rectangle:
#     """ A class to manufacture rectangle objects """

#     def __init__(self, posn, w, h):
#         """ Initialize rectangle at posn, with width w, height h """
#         self.corner = posn
#         self.width = w
#         self.height = h

#     def __str__(self):
#         return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return (self.width + self.height) * 2


# r = Rectangle(Point(0, 0), 10, 5)
# print(r.area() == 50)
# print(r.perimeter() == 30)



# # EXERCISE - 2
# class Person:
#     def __init__(self, name, school, hobby):
#         self.name = name
#         self.school = school
#         self.hobby = hobby

#     def greet(self):
#         return f"Nice to meet you. My name is {self.name}. I am student at {self.school}. I love {self.hobby}"

# bayka = Person("Bayka", "TIU", "Python")
# print(bayka.greet())

# # EXERCISE - 3

from unittest import skip


class Calculator:
    def __init__(self, input_list):
        self.list = []
        for i in input_list:
            self.list.append(int(i))

    def add(self):
        result = 0
        for i in self.list:
            result += i
        
        return result
    
    def subs(self):
        result = self.list[0] * 2
        for i in self.list:
            result -= i

        return result
    
    def multiply(self):
        result = 1
        for i in self.list:
            result *= i

        return result
    
    def divide(self):
        result = self.list[0] ** 2
        for i in self.list:
            result /= i
        return result

# user_input = [600,2,3,4,5,6]
user_input = input("List numbers: ").split(",")
operation = input("Operation (add, subs, multiply, divide): ")
print("Remember, first number will be used for each operation")

calculate = Calculator(user_input)

if operation == "add":
    print(calculate.add())
elif operation == "subs":
    print(calculate.subs())
elif operation == "multiply":
    print(calculate.multiply())
elif operation == "divide":
    print(calculate.divide())
else:
    print("Wrong input")


