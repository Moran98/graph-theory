# Overview of Project

> ###### Version Control : GitHub - Moran98
> ######  Student Name : Aaron Moran
> ###### Student ID : G00356519


## Problem Statement

> You must write a program in the Python programming language [2] that can build a non-deterministic finite automaton (NFA) from a regular expression,and can use the NFA to check if the regular expression matches any given string of text. You must write the program from scratch and cannot use there package from the Python standard library nor any other external library.A regular expression is a string containing a series of characters, some of which may have a special meaning. For example, the three characters.,|,and have the special meanings concatenate,or, and Kleene star respectively.For example, the regular expression0.1means a 0 followed by a 1,0|1meansa 0 or a 1, and1means any number of 1’s. These special characters must be used in your submission.Other special characters you might consider allowing as input are brackets()which can be used for grouping,+which means at least one of, and?which means zero or one of. You might also decide to remove the concatenation character, so that 1.0 becomes 10, with the concatenation implicit. You may initially restrict the non-special characters your program works with to 0 and1. However, you should at least attempt to expand these to all the digits,and the characters at oz, and A to Z.


## Introduction



In this document i will be going into detail about the creation of my project and the source code. The bulk of my projects code can be found in the following repository :

````
 Project/script.py
````

Within this repository there is many functions which I will go into detail about.

* Matching
* Compiling
* Shunting
* Command line arguments.
* Menu Options & User Prompt

## Regular Expressions

Regular Expressions are a sequence of characters that define a search pattern which when implemented in programming can display specific strings from a bulk of text (e.g email addresses). It's main purpose is to find text within a file and is usually built in to every text editor!

My Regex examples (GitHub)
#### Basic RegEx

    ' ^ ' - The beginning of a line.
    ' . ' - Any character.
    ' | ' - The OR operator.
    ' ? ' - Matches the character before the '?' (zero OR one).
    ' + ' - Matches character before '+' (one OR more).
    ' * ' - Matches everyhting in place of the Kleene Star.


## Matching
Within this function we are testing to see if the input Infix will match the input String. The match function receives 2 arguments, and will return true if we get a successful match.

Below we are looping through the characters input for String. We are keeping track of our position at each iteration. If the label of the state matches the character that has been read, add the state that is being pointed at to the current set.

> # 
    for c in s:
        previous = current
        current = set()
        for state in previous:
            if state.label is not None:
                if state.label == c:
                    followes(state.edges[0], current)

##### _Conclusion_
Our matching function is the final step for the program. Once performed correctly we can determine if there was a successful match or not.

## Compiling

This function plays a role as one of the most important in the project. This function determines the start and accept states depending on the Regular Expressions that have been passed into the program.

Firstly we are popping fragments off of the stack, depending on the regular expression you will need to pop more fragments than others. We then determine the start and accept states of the position. Next we are pointing to the new accept start from the old accept state acting as a pointer. 

If we assign the popped fragments to a new instance of the fragment we can determine when testing which operators were popped from the compiler. This can be beneficial when testing so you can see what actions are being taken at the required locations of the infix.

Below is an example snippet from the source code :

>     if c == '.':
            frag = nfa_stack.pop()
            frag1 = nfa_stack.pop()
            frag1.accept.edges.append(frag.start)
            newfrag = Fragment(frag1.start, frag.accept)
            print("Created fragment with '.' operator : ", newfrag)



## Shunting

Within our project we used the Shunting Yard Algorithm to parse the expression in infix notation to produce a prefix notation String.

We used two methods to remove and add to the lists :

* Pop() -  Removes elements.

* Append() -  Adds elements.

Within our Shunting function we initially start by removing any round bracket parenthesis that exist in the Infix by popping them from the list. e.g '(a.b)'

We are then appending any popped operators from the input to the operator stack. We are doing this because we wish to get a matching string and any output with operators still remaining inside will not be a successful match. Any remaining characters are appended to the output list.

>  
      
      elif c in prec:
        while opers and  prec[c] < prec[opers[-1]]:
             postfix.append(opers.pop())
         opers.append(c)
      else:
          postfix.append(c)


##### _Conclusion_

Our shunting method is essential for adding and removing unwanted elements from the infix to achieve a matching String. Any mistakes while shunting can provide an incorrect output so it is necessary to have precise accuracy while shunting.

## Command Line Arguments

As an addition to the project we are required to add command line arguments which can be used to test the program from the command line alone. These arguments exist in almost any command line based programs and are quite simple to implement. 

The sole purpose is to give to user some instructions on the go if they require assistance on what is required to execute the program.

##### Import Used  :

````
import argparse
````

Withing the project i created a function that would execute the command line arguments when requested by the user. The following command can be typed to access the help section :

> python script.py -h / --help

You will then see that i have assigned 2 positional arguments (infix , String)  that are required to perform the command line execution. Once the user provides the program the two arguments that they wish to test the program should execute and display if there was a successful match or an unsuccessful match.

>   if(match(args.infix, args.string))

##### _Conclusion_

By adding argparse to your project it adds more functionality and usability for the user. For such a basic implementation it is absolutely worthwhile to achieve this functionality.


## Menu Options & User Prompt

This section is self explanatory , I have coded a command line UI which the user is prompted to enter an infix and then a string to test the match. The program is then executed and whether or not there is a successful match or not the user is again prompted if they wish to test another or not. If not then the program will exit.

Below is the Menu UI from from source code :

>  

       while x.casefold() not in 'n':
           user_input = input("Enter an infix :")
           string_match = input("Enter a string to match :")
           print("The match was : ", match(user_input, string_match))
           print("===============GraphTheory===============")
           x = input("Would you like to Test another? [y/n]")
       print("Exiting Program...")