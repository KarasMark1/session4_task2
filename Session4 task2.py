def calculator(a, b, operation):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        if b!= 0:
            return a/b
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
print(calculator(12,4,'*'))