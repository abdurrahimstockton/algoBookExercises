#A program to reverse the letters of a word/phrase

from SimpleStack import * #main branch
stack= Stack(100)   #Create a stack to hold letters

word=input("Word to reverse: ")
for letter in word:  #Loop over letters in word
    if not stack.isFull():  #push letters on stack if not full
        stack.push(letter)

reverse=''   #Build the reverse version
while not stack.isEmpty():  #by poping the stack until empty
    reverse+=stack.pop()
print(f"The reverse of {word} is : {reverse }")
