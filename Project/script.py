from G00356519 import *
import re

# Calling G00356519.py for header
g00 = Account()

# # The Input
infix = "(a|b).c*"
print("REGEX is : ", infix)
print("-----------------------------------------")
# Convert input to a stack-ish list
infix = list(infix)[::-1]

#creating lists
stack = [] # LIFO - [operators]
queue = [] # FIFO - [numbers]
# Operator Precedence.
prec = {'*': 5, '.': 4, '|': 3, ')': 2, '(': 1}

while infix:
    # Pop() -  removes and returns last object from the list
    x = infix.pop()

    # remove '(' and ')' operators
    if x == '(' or x == ')':
        # Push and append to the opertor stack
        stack.append(x)
        stack.pop()

    elif x in stack:
        # pushing operators to the stack
        stack.append(x)
        print("Added to Stack : ", stack)

    else:
        # pushing chars to the queue
        queue.append(x)
        print("Added to Queue : ", queue)
print("===========================================")
print(stack)
print(queue)


# Pop all operators to the output
while stack:
    queue.append(stack.pop())

# Convert output list to String
queue = ''.join(queue)

print("Expected Output : ab|c*.")

# Print the result
print("The Output is : ", queue)
