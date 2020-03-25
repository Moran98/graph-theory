from G00356519 import *

# Calling G00356519.py for header
g00 = Account()

# Prefic input list
lPrefix = ['(', 'a', '|', 'b', ')', '.', 'c', '*']

# Using list comprehension to convert to String
prefix = ''.join([str(elem) for elem in lPrefix])

# List to String output
print("The prefix : ",prefix)

# Expected output : "ab|c*."
print("Expected: ", "ab|c*.")

# Operator stack
opers = []

# Output list
pfix = []

# Operator Precedence.
prec = {'*': 100, '.': 80, '|': 60, ')': 40, '(': 20}

# Convert output list to String
pfix = ''.join(pfix)

# Print the result
print("The Output is : ", pfix)
