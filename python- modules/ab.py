# Approach 1: Direct import
# import a
# import b
#
# obj1 = a.Animal()  # object creation
# obj1.display()   # Animal class
#
# obj2 = b.Bird()
# obj2.display()   # Bird class

# *****************************************************************************

# Approach 2:
from a import Animal
from b import Bird

obj1 = Animal()
obj1.display()  # Animal class

obj2 = Bird()
obj2.display()  # Bird class