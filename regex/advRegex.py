# Aaron Moran
# Advanced regular Expressions
#
#
import re

text = open("LoremIpsum.txt", "r")

# Debug to test file open+read
# print(text.read())

# For loop to execute the RegEx and print the result's from each line 
for line in text:
    line = line.rstrip()
    if re.search('^A.+$', line):
        print(line)


# References - https://youtu.be/e0xL9o5VibU - Max Goodridge