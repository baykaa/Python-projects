# class Bike:
#     name = ""
#     gear = 0

# class Person:
#     pass

# Object = Person()
# # print(Object)
# # print(Person)

# class Students:
#     name = ""
#     grade = 0

# Student1 = Students()

# Student1.grade = 11
# Student1.name = "Bayanmunkh Delgersaikhan"

# print(f"Name: {Student1.name}, grade: {Student1.grade} ")

# class Employee:
#     employee_id = 0

# employee1 = Employee()
# employee2 = Employee()

# employee1.employee_id = 1001
# print(f"Employee ID: {employee1.employee_id}")

# employee2.employee_id = 1002
# print(f"Employee ID: {employee2.employee_id}")

# class Animal:
#     name = ""
#     type = ""
#     age = 0

# lion = Animal()
# lion.name = "Simba the King"
# lion.type = "Lion and predator"
# lion.age = 4

# print(f"{lion.name} is {lion.type} and he is {lion.age} years old!")

# class Car:
#     name = ""
#     type = ""
#     year = 0
#     owner_name = ""
#     insurance = ""

# macqueen = Car()
# macqueen.name = "Lighting McQueen"
# macqueen.type = "C6. R Corvette"
# macqueen.year = 20
# macqueen.owner_name = "Bayka"
# macqueen.insurance = True

# if macqueen.insurance:
#     macqueen.insurance = "Insuranced"
# else:
#     macqueen.insurance = "No insurance"

# print(f"{macqueen.name} is {macqueen.type} car. His owner is {macqueen.owner_name}, which he bought him when he was {macqueen.year}. And it is {macqueen.insurance}")

# class Student:
#     def __init__(self, name = "", grade = 0):
#         self.name = name
#         self.grade = grade

# Student1 = Student("Bayka", 100)
# print(f"{Student1.name}, grade: {Student1.grade}")

# class Student:
#     def __init__(self, name, percentage):
#         self.name = name
#         self.percentage = percentage
#     def show(self):
#         print("Name is", self.name, "and percentage is:", self.percentage)
    
# stud = Student("Bayka", 177)

# stud.show()

# class Person:
#     def __init__(self, fname = "Bayka", lname = "Delgersaikhan", age = 22, country = "Mongolia", city = "Ulaanbaatar"):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.country = fname
#         self.city = city
#         self.skills = []
#     def person_info(self):
#         return f"{self.fname} {self.lname} is {self.age} years old. He lives in {self.city}, {self.country}"
#     def add_skills(self, skill):
#         self.skills.append(skill)
    
# p1 = Person()
# print(p1.person_info())
# p1.add_skills('Python')
# p1.add_skills('PHP')
# p1.add_skills('Laravel')
# p1.add_skills('mySQL')
# print("skills:", p1.skills)

# p2 = Person("Maarii", "Urandush", 21, "Mongolia", "UB")
# print(p2.person_info())
# print("skills:", p2.skills)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Person(name={self.name}, age={self.age})"
    
#     def __repr__(self):
#         return f"Person('{self.name}', {self.age})"

# person = Person("John", 30)

# print(person)
# print(str(person))
# print(repr(person))

# EXERCISE 1
# class Vehicle:
#     def __init__(self):
#         pass

# bmw = Vehicle()
# print(bmw)

# EXERCISE 2
class Waiter:
    def __init__(self, name = "", age = 0, gender = ""):
        self.name = name
        self.age = age
        self.gender = gender
    
maarii = Waiter("Maralgue", 34, "they/them")
# print(maarii)
# print(maarii.name)
# print(maarii.age)
# print(maarii.gender)
# print(car2.max_speed, car2.mileage)

# EXERCISE 3
# import numpy
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     def perimeter(self):
#         return (self.length + self.width) * 2
#     def area(self):
#         return (self.length * self.width)
#     def display(self):
#         perimeter = self.perimeter()
#         area = self.area()
#         print(f"Length: {self.length}, Width: {self.width}, Perimeter: {perimeter}, Area: {area}")
# rec1 = Rectangle(4,5)

# print("Perimeter:",rec1.perimeter())
# print("Area:", rec1.area())
# rec1.display()

# # EXERCISE 4
# class BankAccount:
#     def __init__(self, acc_num = 0, acc_name = "", balance = 0):
#         self.acc_num = acc_num
#         self.acc_name = acc_name
#         self.balance = balance
#     def deposit(self, amount_deposit):
#         self.balance += amount_deposit
#     def withdrawal(self, amount_withdrawal):
#         self.balance -= amount_withdrawal
#     def bankFees(self):
#         return self.balance * 0.05
#     def display(self):
#         bank_fee = self.bankFees()
#         return f"Current total balance: {self.balance}, this year fee: {bank_fee}"

# bayka_account = BankAccount(1456, "Yucho bayka", 50000)
# print(f"Current balance: {bayka_account.balance}")
# bayka_account.deposit(10000)
# print(f"Current balance: {bayka_account.balance}")
# bayka_account.withdrawal(45000)
# print(f"Current balance: {bayka_account.balance}")
# print(bayka_account.display())






