# Stack Implementation with Expression Conversion & Evaluation

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Helper: Check if character is operand
def is_operand(ch):
    return ch.isalpha() or ch.isdigit()

# Helper: Operator precedence
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

# Infix to Postfix
def infix_to_postfix(expr):
    stack = Stack()
    output = []
    for char in expr:
        if char == ' ':
            continue
        if is_operand(char):
            output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # Operator
            while (not stack.is_empty() and 
                   stack.peek() != '(' and
                   precedence(stack.peek()) >= precedence(char)):
                output.append(stack.pop())
            stack.push(char)
    
    while not stack.is_empty():
        output.append(stack.pop())
    
    return ''.join(output)

# Evaluate Postfix (for single-digit numbers only)
def evaluate_postfix(expr):
    stack = Stack()
    for char in expr:
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a // b)
    return stack.pop()

# Example usage
if __name__ == "__main__":
    infix = "A+B*C"
    postfix = infix_to_postfix(infix)
    print("Infix:", infix)
    print("Postfix:", postfix)  # Output: ABC*+

    # Numeric example
    numeric_infix = "2+3*4"
    numeric_postfix = infix_to_postfix(numeric_infix.replace('', ' ').replace('  ', ' ').strip())
    # For simplicity, use: "234*+" manually
    result = evaluate_postfix("234*+")
    print("234*+ =", result)  # Output: 14