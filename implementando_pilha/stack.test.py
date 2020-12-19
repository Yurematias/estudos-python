from stack import Stack

stack = Stack(5)

print(stack.asArray)

stack.push('A')
stack.push('B')

print(stack.length) # deve ser 2
print(stack.top) # deve ser B
print(stack.top) # deve ser B

print(stack.pop()) # deve ser B
print(stack.top) # deve ser A
print(stack.pop()) # deve ser A

stack.push('C')
stack.push('D')
stack.push('E')
stack.push('F')
stack.push('G')
stack.push('H') # não entra
print(stack.asArray)

print('----------------')
print(stack.is_empty)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.asArray)
print(stack.is_empty)
