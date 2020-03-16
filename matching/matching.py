# Aaron Moran
# Matching Regular Expressions
#
import re

textSearch = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567891011121314151617181920

Hello World.

My Name is Aaron.

// list URL's
https://www.netflix.com/browse
https://ethereum.org/

- ' [ ] { } / ? \ @ # ~ + - * ^ $ % .
             """

sentence = 'Start a sentence and bring it to an end.'


print("=============================================================")
print("MATCHING SENTENCES IN REGEX")
print("=============================================================")

# Detemine pattern to match and compile
pattern = re.compile(r'\w')

matches = pattern.finditer(textSearch)

for match in matches:
    print(match)

# Parsing text file from data
with open('data.txt', 'r',  encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    # for
    for match in matches:
        print(match)