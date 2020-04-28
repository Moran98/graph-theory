# Overview of Project
In this document i will be going into detail about the creation of my project and the source code. The bulk of my projects code can be found in the following repository :

````
 Project/script.py
````

Within this repository there is many functions which I will go into detail about.

* Match
* Compiling
* Shunting
* Command line arguments.
* User Prompt
* Menu Options

### Match
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

### Compile

This function plays a role as one of the most important in the project. This function determines the start and accept states depending on the Regular Expressions that have been passed into the program.