# Build Your Own Python Calculator Today

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

if op == '+':
    print(x + y)
elif op == '-':
    print(x - y)
elif op == '*':
    print(x * y)
elif op == '/':
    print(x / y if y != 0 else "Error! Division by zero.")
else:
    print("Invalid operation")
