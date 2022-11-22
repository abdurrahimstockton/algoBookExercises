from SimpleStack import *
stack=Stack(100)

for word in ['May','the', 'force', 'be', 'with', 'you']:
    stack.push(word)

print(f"After pushing {len(stack)} words on the stack, contains: \n {stack}")
print(f"Is stack full: {stack.isFull()}")

print(f"Popping items of the stack: ")
while not stack.isEmpty():
    print(f"{stack.pop()}", end=' ')
print()
