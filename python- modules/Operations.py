# Approach 1
# import Calculator
# Calculator.add(100, 200)  # 300
# Calculator.mul(10, 20)   #200

# # Approach 2 : importing only specific functions
# from Calculator import mul
# mul(50, 3)  # 150

# Approach 3 : importing all  functions
from Calculator import *
mul(10, 3)  # 30
