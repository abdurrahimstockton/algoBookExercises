# A program to check that delimiters are balanced in an expression

from SimpleStack import *
stack= Stack(100)  #Create a stack to hold delimiter tokens

expr= input("Expression to check: ")
errors=0 #Assume no errors in expression

for pos, letter in enumerate(expr): # loop over letters in expression
    if letter in "{[(": #Look for starting delimiter
        if stack.isFull(): #A full stack means we can't continue
            raise Exception(f"Stack overflow on expression ")
        else:
            stack.push(letter) #put left delimiter on stack

    elif letter in "}])": #Look for closing delimiter
        if stack.isEmpty(): #If stack is empty, no left delimiter
            print(f"Errors: {letter} at position {pos} has no matching left delimiter")
            errors+=1

        else:
            left=stack.pop()    #Get left delimiter from stack
            if not (left=="{" and letter=="}" or #Do delimiters match?
                    left=="[" and letter=="]" or
                    left=="(" and letter==")"):
                print(f"Error: {letter} at position {pos} doesn't match left delimiter {left}")
                errors+=1

#After going through entire epxression, check if stack empty
if stack.isEmpty() and errors==0:
    print(f"Delimiters balance in expression : {expr}")

elif not stack.isEmpty(): #Any delimiters on stack weren't matched
    print(f"Expression missing right delimiters for {stack}")
