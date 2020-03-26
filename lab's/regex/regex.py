# Aaron Moraan
# Learning and Practicing the basics within Regular Expressions && Python. 
#
#
import re

myString = 'Hello, my name is Aaron Moran and i am a 3rd year Software Developmetn Student.'
sampleText = """My name is Aaron, I am 21 years old, my email address is : aaron@gmail.com,
                 John Doe , email address is john@gmail.com, Mary email address is mary@gmail.com,
                 Students name, email address is student@gmail.com, GMIT email address is GMIT@gmail.com
             """


# Debug test to make sure all is working okay
print(myString)

# Printing numbers 0-9, all lowercase letters, all higher case characters and syntax
result = re.findall('[0-9]', myString)
result1 = re.findall('[a-z]', myString)
result2 = re.findall('[^a-z]', myString)
# Extract email from text
result3 = re.findall('\S+@\S+',  sampleText)

# Find and Print list from Regular Expression
print(result)
print(result1)
print(result2)
# Print list of all emails from sample text
print(result3)

# References - https://youtu.be/e0xL9o5VibU - Max Goodridge