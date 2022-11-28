# # Approach 1:
# import sys
# sys.path.append("C:/Users/User/PycharmProjects/Learn Python/python - packages/package1")
# sys.path.append("C:/Users/User/PycharmProjects/Learn Python/python - packages/package1/package2")
#
# import module1
# import module2
#
# module1.display()   # this is display() from module 1
# module2.show()      # this is show() from module 2

# *****************************************************************************

# Approach 2:
import sys
sys.path.append("C:/Users/User/PycharmProjects/Learn Python/python - packages/package1")
sys.path.append("C:/Users/User/PycharmProjects/Learn Python/python - packages/package1/package2")

from module1 import *
from module2 import *

display()    # this is display() from module 1
show()       # this is show() from module 2