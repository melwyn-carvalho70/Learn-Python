import sys

sys.path.append("C:/Users/User/PycharmProjects/Learn Python/python - packages/pack 1")   # importing the package

# Approach 1:
# import module1
# import module2
#
# module1.display()   # this is display() from module
# module2.show()      # this is show() from module 2



# Approach 1:
from module1 import *
from module2 import *

display()     # this is display() from module 1
show()        # this is show() from module 2
