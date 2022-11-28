import sys
sys.path.append("C:/Users/User/PycharmProjects/Learn Python/python - packages/p1")
sys.path.append("C:/Users/User/PycharmProjects/Learn Python/python - packages/p2")

from empmod import *
empobj = Employee(1, "John", 20000)
empobj.displayemp()   # 1 John 20000

from stumod import *
stuobj = Student(12, "Peter", "A")
stuobj.displaystu()   # 12 Peter A