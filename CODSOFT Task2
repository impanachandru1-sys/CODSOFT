import math
print("=== Scientific Calculator===")
print("operation: + - * / sin cos tan log sqrt pow")
while True:
    op=input("\nEnter operation (or 'exit' to quit):")
    if op=="exit":
        print("Calculator Closed.")
        break
    if op in["sin","cos","tan","log","sqrt"]:
        num=float(input("Enter Number:"))
        if op=="sin": print("Result=", math.sin(math.radians(num)))
        elif op=="cos": print("Result=", math.cos(math.radians(num)))
        elif op=="tan": print("Result=", math.tan(math.radians(num)))
        elif op=="log":
            if num > 0: print("Result=", math.log(num))
            else: print("Error! Log undefined.")
        elif op == "sqrt":
            if num >= 0: print("Result=", math.sqrt(num))
            else: print("error! Negative number.")
    elif op in["+","-","*","/","pow"]:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if op== "+": print("Result=", num1 + num2)
        elif op== "-": print("Result=", num1 - num2)
        elif op== "*": print("Result=", num1 * num2)
        elif op== "/":
            if num2 != 0: print("Result =", num1 / num2)
            else: print("Error! Division by zero.")
        elif op == "pow": Print("Result =", math.pow(num1, num2))
    else:
        print("Invalid Operation! Try again.")
        
  
     

  
     

        
  
     

  
     
