# Same function 2 modules:
# Approach 1: using the module name with the function name
# import Animal
# import Bird
# Animal.fly()  # Animal cant fly
# Animal.color()  # Animal is black
#
# Bird.fly()  # Bird can fly
# Bird.color()  # Bird is green

# *****************************************************************************

# Approach 2: The latest imported will be executed
# from Animal import *
# fly()
# color()
#
# from Bird import *
# fly()   # Bird can fly - since bird is imported the latest
# color()  # Bird is green