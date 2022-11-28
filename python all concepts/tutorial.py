# this is a single line comment
"""This
is a  multiline comment """


# Keywords
# import keyword
# print(keyword.kwlist)


# data types
# x=10
# y=20.2
# z= "John"
# print(type(x), type(y), type(z))


# # variables declaration
# a, b, c = 10, 20.5, "melwyn"
# print(a, b, c)


# deleting variables
# a=10
# b=20
# print(a, b)
# del(a)
# print(a, b)

# ---------------------------------------------------------------------------------------------------------------------

# Arithmetic Operators
# a=5
# b=2
# print(a//b)  # quotient
# print(a % b)  # Remainder
# print(a**b)  # a^b

# *****************************************************************************

# Logical Operators ( and or not )


# Concatenation ( +)
# print(10+10)
# print(10.5 + 12.0)
# print(10+10.5)
# print('welcome' + 'python')
# print(True + 5, False + 5)  # True = 1 False = 0
# print(True + True, False + False)

# ---------------------------------------------------------------------------------------------------------------------

# Print Formatting output
# name, age, salary = 'john', 13, 100.35
# print("name is :%s Age is :%d Salary is :%g" % (name, age, salary))
# print("name is :{} Age is :{} Salary is :{}" .format(name, age, salary))


# Taking input from the user and typecast ( int() float() )
# no1 = int(input(" Enter first number:"))  # converting it to int from str
# no2 = int(input("enter second number:"))  # converting it to int from str
# no1 = input(" Enter first number:")
# no2 = input("enter second number:")
# print(type(no1), type(no2))  # will display type as str by default
# print(int(no1) + int(no2))  # convert to int and add

# ---------------------------------------------------------------------------------------------------------------------

# Control statements
# Conditional statements (if, if else, elif )

# Example 1  ( person eligible for vote)
# age = 20
# if age >= 18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")

# Example 2
# if 1:
#     print("ONE")
# else:
#     print("Not ONE")

# Example 3
# num = 10
# if num % 2 == 0:
#     print("Even")
# else:
#     print("ODD")

# Example 4 : if else single line
# num = 10
# print("even number") if num % 2 == 0 else print("odd number")

# Example 5: multiple statements on a single line
# num = 5
# {print("even number"), print(num)} if num % 2 == 0 else {print("odd number"), print(num)}

# Example 6 : elif
# week = 1
# if week == 1:
#     print("sunday")
# elif week ==2:
#     print("Monday")
# elif week == 3:
#     print("tuesday")
# elif week == 4:
#     print("wednesday")
# else:
#     print("invalid")

# ---------------------------------------------------------------------------------------------------------------------

# Looping Statements: while and for
# range() function in python using list()
# print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(1, 10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]
# print(list(range(10, 1, -1)))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# While loop
# Example 1: to print 1 to 10 in descending order
# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1

# *****************************************************************************

# For loop
# Example 1: to print even nos from 1 to 20
# for i in range(0, 21, 2):    # value of the range gets assigned to i via the in operator
#     print(i)

# Example 2: to print 1 to 10 in descending order
# for i in range(10, 0, -1):    # value of the range gets assigned to i via the in operator
#     print(i)

# *****************************************************************************

# Jumping Statements: break and continue
# break continue
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)
# print("Program exited!!")

# for i in range(1, 10):
#     if i == 3 or i == 5 or i == 7:
#         continue  # print will be skipped and i=3 5 7 will not be printed
#     print(i)
# print("Program exited!!")

# ---------------------------------------------------------------------------------------------------------------------

# Numbers & Strings:
# Example 1: maximum of nos using max() and minimum using min()
# print(" max no is:", max(10, 20, 70, 50, 90, 30))
# print(" min no is:", min(10, 20, 70, 50, 90, 30))

# creating a string
# s = "hello"
# s = 'hello'
# s = str("hello")
# s = str('hello')

# Operations on Strings:
# mutable - cannot change the ID value of variable. Strings are im-mutable
# Immutable - can change the ID value of variable (string).

# Example 1
# str1 = "welcome"
# print(id(str1))  # ID 3218395281264
# str1 = str1 + "home"
# print(id(str1))  # ID 3218395329072

# Example 2: + and * with string
# str = "welcome "
# print(str + "programming") # concat
# print(str * 2)  # * is used to print multiple times

# Slicing a string [] : starting index is 0 , ending index is 1
# Example 3
# str1 = "welcome"
# print(str1[1:3])  # el  1-e, 3-from e to l
# print(str1[:6])  # welcom 0-w, 6-from w to m
# print(str1[2:])  # lcome 2-l, blank is end so l to e
# print(str1[1:-1])  # elcom -1 removes last character
# print(str1[1:-2])  # elco -2 removes last 2 characters

# Example 4: ord() and chr()
# print(ord("A"))  # prints the ascii value of A = 65
# print(chr(65))  # prints the value associated to the ascii 65 = A

# Example 5: max() min() and len()
# print(max("abc"))  # c is max
# print(min("abc"))  # a is min
# print(len("welcome"))  # length of string is 7

# Example 6 : in and not in operator - returns true or false
# s = 'welcome'
# print("come" in s)  # true
# print("some" in s)  # false
# print("come" not in s)  # false

# Example 7 : string comparison
# print("abc" == "ABC")  # false
# print("abc" != "ABC")  # true
# print("arrow" > "aron")  # true

# Example 8 : testing string functions
# s = "welcome to python"
# print(s.isalnum())  # all num or not
# print(s.isalpha())  # all alphabets or not
# print("2022".isdigit())  # all digits or not
# print("print".isidentifier())  # if the string is an identifier/keyword
# print(s.islower())  # all lower case or not
# print("HEY".isupper())  # all upper case or not
# print(" ".isspace())   # all spaces or not

# Example 9 : searching for substring functions
# s = "welcome to python"
# print(s.endswith("thon"))  # if string ends with the string in the function
# print(s.startswith("hey"))  # if string start with the string in the function
# print(s.find("come"))  # returns position of the string 3 if found
# print(s.find("no"))  # returns -1 if not found
# print(s.count("d"))  # counts no of times d is there, either 0 or x times

# Example 10: Converting strings
# s = "String in PYTHON"
# print(s.capitalize())  # String in python - removes capitalization of a full word
# print(s.title())  # String In Python -  first letter capital
# print(s.lower(), s.upper())  # string in python - full string to lower, STRING IN PYTHON - full string to upper
# print(s.swapcase())  # sTRING IN python - swap the entire strings cases
# print(s.replace(" in", " for")) # String for PYTHON - changes in to for

# Example 11 : Reverse a string
# Method 1:
# s = "welcome"
# reverse_s = ""
# for i in s:
#     reverse_s = i + reverse_s
# print("reverse is:", reverse_s)  # reverse is: emoclew

# Method 2:
# s = "welcome"
# reverse_s = s[::-1]  # s[0:all:-1]
# print("reverse is:", reverse_s)   # reverse is: emoclew

# ---------------------------------------------------------------------------------------------------------------------

# Collections :  list, tuple, set, dictionary
# List: ordered and changeable [ ]
# Example 1 : create a list
# mylist1 = [ 10, 20, 30, 40, 50]
# mylist2 = ['apple', 'banana', 'cherry']
# mylist3 = [ 'apple', 30, 'banana', 40]
# mylist = list()
# print(mylist)
# print(mylist1)
# print(mylist2)
# print(mylist3)

# Example 2: accessing items from the list
# mylist = ['apple', 'banana', 'cherry']  # index starts from zero
# print(mylist[0])  # apple
# print(mylist[1])  # banana
# print(mylist[2])  # cherry
# print(mylist[-1])  # cherry

# Example 3 : range of indexes
# mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
# print(mylist[2:5])  # ['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])  # ['orange', 'kiwi', 'melon']

# Example 4 : changing items from list
# mylist = ['apple', 'banana', 'cherry']
# print(mylist)  # ['apple', 'banana', 'cherry']
# mylist[0] = 'orange'
# print(mylist)  # ['orange', 'banana', 'cherry']

# Example 5 : read items using loops
# mylist = ['apple', 'banana', 'cherry']
# for i in mylist:
#     print(i)

# Example 6 : check if item exists in the list
# mylist = ['apple', 'banana', 'cherry']
# if 'apple' in mylist:
#     print('yes it is present')
# else:
#     print('not present')

# Example 7: length of a list
# mylist = ['apple', 'banana', 'cherry']
# print(len(mylist))  # 3

# Example 8 : add items - append() and insert()
# mylist = ['apple', 'banana', 'cherry']
# mylist.append('orange')  # added new item orange
# print(mylist)  # ['apple', 'banana', 'cherry', 'orange']
# mylist.insert(1, 'mango')  # inserted mango at position 2
# print(mylist)  # ['apple', 'mango', 'banana', 'cherry', 'orange']

# Example 9 : remove items from list - pop(), del, clear()
# mylist = ['apple', 'banana', 'cherry']
# mylist.pop(0)  # specify index no
# print(mylist)  # ['banana', 'cherry']
# del mylist[1]  # delete cherry
# print(mylist)  # ['banana']
# mylist = ['apple', 'banana', 'cherry']
# print(mylist)
# mylist.clear()  # clears all
# print(mylist)  # []

# Example 10 : copy items into another list - list(), copy()
# mylist1 = ['apple', 'banana', 'cherry']
# mylist2 = list(mylist1)  # list() function is used to copy
# print(mylist1, mylist2)  # ['apple', 'banana', 'cherry'] ['apple', 'banana', 'cherry']
# mylist3 = mylist1.copy()  # copy the contents into mylist3
# print(mylist3)  # ['apple', 'banana', 'cherry']

# Example 11 : combine or join lists
# Using the + operator
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)  # ['a', 'b', 'c', 1, 2, 3]

# Using loops
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# for i in list2:
#     list1.append(i)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# Using extend()
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# *****************************************************************************

# Tuple : ordered and unchangeable ()
# Example 1 : creating
# mytuple = ('apple', 'banana', 'cherry')
# print(mytuple)  # ('apple', 'banana', 'cherry')

# Example 2 : access tuple items
# mytuple = ('apple', 'banana', 'cherry')
# print(mytuple[1])  # banana
# print(mytuple[-1])  # cherry

# Example 3 : range of indexes
# mytuple =('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
# print(mytuple[2:5])  # ('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1])  # ('orange', 'kiwi', 'melon')

# Example 4 : change tuple values (cannot change directly)
# mytuple = ('apple', 'banana', 'cherry')
# mylist = list(mytuple)  # converted the tuple into a list using list()
# mylist[0] = 'orange'
# mytuple = tuple(mylist)  # converting the list back to a tuple using tuple()
# print(mytuple)  # ('orange', 'banana', 'cherry')

# Example 5 ; reading tuple items using loop
# mytuple = ('apple', 'banana', 'cherry')
# for i in mytuple:
#     print(i)

# Example 6 : check i item exists
# mytuple = ('apple', 'banana', 'cherry')
# if 'banana' in mytuple:
#     print("yes")
# else:
#     print("No")

# Example 7 : tuple length :
# mytuple = ('apple', 'banana', 'cherry')
# print(len(mytuple))  # 3 items in the tuple

# Example 8 : copy items from 1 tuple into  another tuple
# mytuple1 = ('apple', 'banana', 'cherry')
# mytuple2 = mytuple1
# print(mytuple2)  # ('apple', 'banana', 'cherry')

# Example 9 : join / combining 2 tuples
# tuple1 = (10, 20, 30)
# tuple2 = ('a', 'b', 'c')
# tuple3 = tuple1 + tuple2  # concat operator + used
# print(tuple3)  # (10, 20, 30, 'a', 'b', 'c')

# Example 10 : check if 2 tuples are equal or not
# tuple1 = (10, 20, 30)
# tuple2 = ('a', 'b', 'c')
# if tuple1 == tuple2:
#     print("equal")
# else:
#     print("not equal")  # executed

# *****************************************************************************

# Set : unordered and un-indexed
# Example 1:
# myset = {'apple', 'banana', 'cherry'}
# print(myset)  # {'apple', 'cherry', 'banana'}

# Example 2: Accessing items from set
# myset = {'apple', 'banana', 'cherry'}
# for i in myset:
#     print(i)

# Example 3: Check if items exist in set
# myset = {'apple', 'banana', 'cherry'}
# print("banana" in myset)  # True

# Example 4: adding items to set
# add() - single item  update() - multiple items
# myset = {'apple', 'banana', 'cherry'}
# # myset.add('orange') # {'cherry', 'banana', 'apple', 'orange'}
# myset.update(['mango', 'grapes'])
# print(myset)  # {'mango', 'cherry', 'banana', 'apple', 'grapes'}

# Example 5: find number o items in a set
# myset = {'apple', 'banana', 'cherry'}
# print(len(myset))  # 3

# Example 6: remove items from set - remove() and discard()
# myset = {'apple', 'banana', 'cherry'}
# myset.remove('banana')
# print(myset)  # {'cherry', 'apple'}
# myset.discard('apple')
# print(myset)  # {'cherry'}

# Example 7: clear all items from set
# myset = {'apple', 'banana', 'cherry'}
# myset.clear()
# print(myset)  # set()
# del myset  # delete the set completely

# Example 8: joining 2 sets - union()
# set1 = {'a', 'b', 'c'}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)  # {1, 2, 3, 'b', 'a', 'c'}

# update()
# set1 = {'a', 'b', 'c'}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)  # {'b', 1, 2, 3, 'c', 'a'}

# *****************************************************************************

# Dictionary: unordered, changeable and indexed {}
# Example 1: creating a dictionary
# mydict = {101: 'x', 102: 'y', 103: 'z'}
# print(mydict)  # {101: 'x', 102: 'y', 103: 'z'}

# Example 2: Accessing items from the dictionary
# mydict = {"brand": "Hyundai",
#           "model": "i10",
#           "year": 2021
#           }
# print(mydict['brand'])  # Hyundai
#
# # using get()
# print(mydict.get("model"))  # i10

# Example 3: Changing values from the dictionary
# mydict = {"brand": "Hyundai",
#           "model": "i10",
#           "year": 2021
#           }
# mydict["year"] = 2022
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2022}

# Example 4 : Reading items from dictionary using loops
# mydict = {"brand": "Hyundai",
#           "model": "i10",
#           "year": 2021
#           }
# for i in mydict:
#     print(i)  # will print only the keys i.e.  brand, model, year
#
# for i in mydict:
#     print(mydict[i])  # will print only the values
#
# for i in mydict.values():
#     print(i)  # here the values are obtained

# for x,y in mydict.items():
#     print(x,y)  # here the entire item is stored and x takes the key and y the value

# Example 5 : Check if key exists in the dictionary or not
# mydict = {"brand": "Hyundai",
#           "model": "i10",
#           "year": 2021
#           }
# if "model" in mydict:
#     print("Exists")  # Exists
# else:
#     print("Not exists")
#
# print("model" in mydict)   # True

# Example 6 : find number of items in the dictionary
# mydict = {"brand": "Hyundai",
#           "model": "i10",
#           "year": 2021
#           }
# print(len(mydict))  # 3

# Example 7 : Adding  and removing items
# mydict = {"brand": "Hyundai",
#           "model": "i10",
#           "year": 2021
#           }
# mydict["color"] = "red"
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021, 'color': 'red'}
# # mydict.pop("year")
# # print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'color': 'red'}
#
# del mydict["year"]  # delete a specific item
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'color': 'red'}
#
# mydict.clear()
# print(mydict)  # clears all items
# del mydict  # remove the dictionary completely

# Example 8: copying dictionary
# mydict = {"brand": "Hyundai",
#           "model": "i10",
#           "year": 2021
#           }
# without using copy function
# mydict2 = mydict
# print(mydict2)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}

# Using copy()
# mydict1 = mydict.copy()
# print(mydict1)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}

# ---------------------------------------------------------------------------------------------------------------------

# Functions :
# Example 1: creation and call
# def funct():   # Function declaration
#     print("hello")
# funct()  # function call

# Example 2: passing parameters
# def myfun(name): arg taken but value printed and not returned
#     print("hello", name)
# myfun("Smith")  # hello Smith

# def cal(a, b): 2 args and returns sum of both
#     return a + b
# print(cal(10,20))   # 30

# Example 3: No args no return
# def funct():
#     i = 10
# print(funct()) # None

# Example 4: takes args but prints instead of returning a value
# def cal(a, b):
#     print(a + b)
# cal(10, 20)

# *****************************************************************************

# Global and local Variables: outside function - global, inside function - local
# Example 1:
# global_var = 20  # global variable
# def funct():
#     local_var = 10  # local variable
#     print(local_var)
#     print(global_var)
# funct()  # 10, 20

# Example 2: same name for global and local
# xy = 100
# def cool():
#     xy = 200
#     print(xy)
# cool()   # 200
# print(xy)   # 100

# Example 3: changing the global variable value inside the function
# xy = 100
# def cool():
#     global xy  # using the global variable
#     xy = 200
#     print(xy)
# cool()   # 200
# print(xy)   # 200

# Example 5:
# def col():
#     global x  # global variable created inside using global keyword
#     x = 500
#     print(x)
# col()  # 500
# print(x)  # 500

# *****************************************************************************

# Arguments / parameters:
# Example 1:
# def fun(i, j):
#     print(i, j)
# # fun(10, 20)  # positional arguments
# fun(j = 20, i = 10)  # keyword arguments (specifying variables with the values)

# Example 2 : default values assigned to positional parameters
# def funct(i, j=10):
#     print(i, j)
# # funct(100, 200)  # 100 200 - default value of j is replaced by 200
# funct(101)  # 101 10 - default value of j is considered

# Example 3 : keyword args
# def greet(name, msg):
#     print(msg+ " " +name)
# greet(msg="hello", name ="John")  # hello John

# Example 4: combo of positional and Keyword args
# def my_funct(a, b, c):
#     print(a, b, c)
# my_funct(10, 20, 30)  # positional parameters 10 20 30
# my_funct(a=10, c=25, b=50)  # Keyword parameters 10 50 25
# my_funct(1, 2, c=9)  # 1 2 9
# my_funct(6, b=12, 3)  # wrong because positional arguments should appear before keyword arguments

# Example 5 : function returning multiple values
# def largest(a, b):
#     if a > b:
#         return a, b
#     else:
#         return b, a
# # print(largest(101,20)) # (101, 20)
# res = largest(10, 20)
# print(res)  # (20, 10)
# print(type(res))   # <class 'tuple'>

# ---------------------------------------------------------------------------------------------------------------------

# OOPS: Class, object, inheritance, polymorphism
# Class :
# Example 1: creation
# class MyClass:
#     def myfun(self):  # Method belongs to the class indicated by self keyword
#         pass   # indicates empty method
#
#     def display(self, name):
#         print(name+ " smith")
#
# mc1 = MyClass()    # object 1
# mc2 = MyClass()   # object 2
# mc1.myfun()  # accessing the methods via the object
# mc1.display("john")  # john smith

# Example 2: Instance vs Static method
# class MyClass:
#     def m1(self):
#         print("Instance method")
#
#     @staticmethod  # annotation: convert to static method (access via class directly)
#     def m2(self, num):
#         print(self, num)
#
# o1 = MyClass()
# o1.m1()   # Instance method
# MyClass.m2(100, 200)  # 100 200 - static method invoked using class name

# Example 3: Class variables and accessing them
# class My:
#     a, b = 10, 20  # Class variables
#
#     def add(self):
#         print(self.a + self.b)  # self is used to access the class variables
#
#     def mul(self):
#         print(self.a * self.b)  # self is used to access the class variables
#
# mc = My()
# mc.add()  # 30
# mc.mul()  # 200

# Example 4: global, local and class variables
# i, j = 15, 25  # i , j are global variables
# class My:
#     a, b = 10, 20   # a, b are class variables
#
#     def add(self, x, y):         # x, y are local variables
#         print(x+y)               # sum of local variables
#         print(self.a + self.b)   # sum of class variables
#         print(i + j)             # sum of global variables
#
# mc = My()
# mc.add(100, 200)  # 300 30 40

# Example 5: global, local and class variables all with same names
# a, b = 15, 25  # a, bare global variables
# class My:
#     a, b = 10, 20   # a, b are  also class variables
#
#     def add(self, a, b):         # x, y are local variables
#         print(a+b)
#         print(self.a + self.b)
#         print(globals()['a'] + globals()['b'])    # globals()[] is used to access the global variables when the name is same

# mc = My()
# mc.add(100, 200)  # 300 30 40

# Example 6: one class with multiple objects
# class My:
#     def display(self, name):
#         print("this is display method")
#         print(name)
#
# obj1 = My()
# obj1.display("john")
#
# obj2 = My()
# obj2.display("scott")

# Example 7: Constructor __init__(self):  - will not return any value, but can accept parameters
# class con:
#     def __init__(self):
#         print("this is contructor")
#
#     def m1(self):
#         print("hello")
#
#     def m2(self, x, y):
#        return (x + y)
#
#
# obj = con()    # on creation of object, contructor is invoked
# obj.m1()       # invoked eplicitly by calling the method
# print(obj.m2(10, 20))  # 30

# Example 8: parameterized constructor
# class Myclass:
#     name = 'John'
#     def __init__(self, name):  # parameterized constructor
#         print(name)
#         print(self.name)
#
# mc = Myclass("Smith")   # value passed because of the parameterized constructor

# Example 9:
# class Emp:
#
#     def __init__(self, eid, ename, sal):
#         self.eid = eid      # converting local variables to class variables
#         self.ename = ename
#         self.sal = sal
#
#     def display(self):
#         print("EID:", self.eid)
#         print("Ename:", self.ename)
#         print("salary:", self.sal)
#
# e1 = Emp(101, "john", 20000)
# e1.display()  # EID: 101   Ename: john   salary: 20000

# Example 10:
# class Emp:
#
#     def __init__(self, eid, ename, sal):
#         self.eid = eid      # converting local variables to class variables
#         self.ename = ename
#         self.sal = sal
#
#     def __str__(self):  # string constructor only returns string data
#         return self.ename
#
# e1 = Emp(101, "john", 20000)
# print(e1)   # used to invoke the string constructor

# *****************************************************************************

# Inheritance : Single , multi-level, hierarchy, multiple
# Example 1: Single inheritance
# class A:
#     def m1(self):
#         print("m1 from  Class A")
#
# class B(A):           # B becomes child of class A
#     def m2(self):
#         print("m2 from  Class B")
#
# bobj = B()
# bobj.m1()  # accessing m1 using obj of class B
# bobj.m2()  # accessing m2 using obj of class B

# Example 2:
# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):     # B becomes child of class A
#     a, b = 200, 100
#     def m2(self):
#         print(self.a - self.b)
#
# bobj = B()
# bobj.m1()  # 30
# bobj.m2()  # 100

# Example 3: Multilevel inheritance
# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):     # B becomes child of class A
#     a, b = 200, 100
#     def m2(self):
#         print(self.a - self.b)
#
# class C(B):    # C becomes child of class B and grandchild of class A
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1()  # 30
# cobj.m2()  # 100
# cobj.m3()  # 10

# Example 4: Hierarchy inheritance (1 parent but multiple children)
# class A:
#     x, y = 10, 20
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):     # B becomes child of class A
#     a, b = 200, 100
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A):    # C becomes child of class A
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
# bobj = B()
# bobj.m1()  # 30
# bobj.m2()  # 100
#
# cobj = C()
# cobj.m1()  # 30
# cobj.m3()  # 10

# Example 5: Multiple inheritance (2 parents but one child)
# class A:     # A becomes parent of class C
#     x, y = 10, 20
#     def m1(self):
#         print(self.x + self.y)
#
# class B:     # B becomes parent of class C
#     a, b = 200, 100
#     def m2(self):
#         print(self.a - self.b)
#
# class C(A, B):    # C becomes child of class A and class C
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
# cobj = C()
# cobj.m1()  # 30
# cobj.m2()  # 100
# cobj.m3()  # 10

# Example 6: Calling parent class method using child class - super()
# class A:
#     def m1(self):
#         print("m1 from class A")
#
# class B(A):
#     def m1(self):   # method overriding ( same method name but different implementation from parent class)
#         print("m1 from class B")
#         super().m1()   # invoking the m1 method from the parent class using super()
#
# bobj = B()
# bobj.m1()  # m1 from class B , m1 from class A

# Example 7:
# class A:
#     a, b = 10, 20
#
# class B(A):
#     i, j = 100, 200
#     def m(self, x, y):
#         print(x+y)               # 3000
#         print(self.i + self.j)   # 300
#         print(self.a + self.b)   # 30
#
# bobj = B()
# bobj.m(1000, 2000)

# Example 8: Variable overriding
# class Parent:
#     name = "scott"
#
# class Child(Parent):
#     name ="john"  # overriding the variable name
#     def test(self):
#         print(super().name)     # accessing the parent class variable
#
# cobj = Child()
# print(cobj.name)   # john
# cobj.test()        # scott

# Example 8: Method overriding
# class Bank:
#     def ROI(self):
#         return 0
#
# class XBank(Bank):
#     def ROI(self):
#         return 10
#
# class YBank(Bank):
#     def ROI(self):
#         return 12
#
# objx = XBank()
# print(objx.ROI())   # 10
# objy = YBank()
# print(objy.ROI())   # 12

# *****************************************************************************

# Polymorphism : overloading
# Example 1 :
# class Human:
#     def hello(self, name=None):
#         if name is not None:
#             print("Hello " +name)
#         else:
#             print("Hello.. ")
#
# h = Human()
# h.hello("scott")   # Hello scott
# h.hello()          # Hello..

# Example 2 :
# class Calc:
#     def add(self, a=0, b=0, c=0):
#         print(a + b + c)
#
#
# calobj = Calc()
# calobj.add()  # 0
# calobj.add(10, 20)  # 30
# calobj.add(100, 200, 300)  # 600

# ---------------------------------------------------------------------------------------------------------------------

# Modules: [python - modules]
# Modules : collection of functions and classes (methods + variables)

# ---------------------------------------------------------------------------------------------------------------------

# Packages: [python - packages]
# Package : collection of modules

# Example 1:
# pack 1 -> module1
# pack 1 -> module2
# clientforpack1

# Example 2:
# package1 -> module1 -> display()
# package1 -> package2 -> module 2 -> show()
# clientpackage1

# Example 3:
# Package      # Module        # Class     # Methods
# p1 ->         empmod ->       Employee ->      displayemp()
# p2 ->         stumod ->       Student ->  displaystu()
# p3 ->         client

# ---------------------------------------------------------------------------------------------------------------------

# Exception handling: try, except,
# Example 1:
# print("this is the start:")
# try:
#     print(x)
# except:
#     print("exception occured")
#
# print("this is the end:")

# Example 2:
# print("this is the start:")
# print("in progress")
# try:
#     print(10/0)
# except ZeroDivisionError:    # if the exception received matches
#     print("program complete")

# Example 3: Multiple except blocks - try, except else, finally
# try:
#     num1 = 10
#     num2 = 5
#     result = num1/num2
#     print("Result is: ", result)
#
# except ZeroDivisionError:
#     print("ZeroDivisionError: division by zero")
#
# except SyntaxError:
#     print("SyntaxError: exception")
#
# except:
#     print("Exception handled..")
#
# else:      # executed if no exceptions are present
#     print("no exception occurred")
#
# finally:    # executes irrespective of exceptions
#     print("always execute")

# Example 4: Raising own exceptions
# def enterage(num):
#     if num < 0:
#         raise ValueError("Only integers allowed")
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("odd")
#
# print("checking number if even or odd")
# num = -1
# try:
#     enterage(num)   # ValueError: Only integers allowed
# except ValueError:
#     print("Value error detected and handled")
#
# print("program complete")

# ---------------------------------------------------------------------------------------------------------------------

# File Handling - working with text files
# Example 1: write to blank file
# file = open("C:/Users/User/OneDrive/Desktop/demo/Myfile.txt",'w')     # open file in writing mode
# file.write("First statement \n")
# file.write("second statement \n")
# file.write("Third statement \n")
# file.close()      # closing the file
# print("program complete")

# Example 2: reading data from text file
# file = open("C:/Users/User/OneDrive/Desktop/demo/Myfile.txt",'r')
# print(file.readline())  # read first line and print - First statement
# print(file.read())    # read all and print
# file.close()

# Example 3: adding(appending) data to text file
# file = open("C:/Users/User/OneDrive/Desktop/demo/Myfile.txt",'a')
# file.write("Fourth statement \n")   #
# file.close()
# print("program completed")

# ---------------------------------------------------------------------------------------------------------------------