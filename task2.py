# TASK 2 CALCULATOR
import sys
import math
def add(a, b):
    answer = a + b 
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def substract(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multiply(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + "= " + str(answer) + "\n")
    
def divide(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + "= " + str(answer) + "\n")
    
def power(x, y):
    answer =  math.pow(x, y)
    print(str(x) + " power of " + str(y) + " =", answer)

def square_root(x):
    answer = math.sqrt(x)
    print("Square root of " + str(x) + " = ", answer)
    
def cube_root(x):
    answer = math.cbrt(x)
    print("Cube root of " + str(x) + " = ", answer)

def log_x(x):
    answer = math.log(x)
    print("Log of " + str(x) + " = ", answer)
    
def exponent_x(x):
    answer = math.exp(x)
    print("Exponent of " + str(x) + " = ", answer)
    
def cosine_x(x):
    answer = math.cos(x)
    print("The cosine of " + str(x) + " = ", answer)
    
def sine_x(x):
    answer = math.sin(x)
    print("The sine of "+ str(x) + " = ", answer)

def tan_x(x):
    answer = math.tan(x)
    print("Tan of " + str(x) + " = ", answer)
    
def acosine_x(x):
    answer = math.acos(x)
    print("Arc cosine of " + str(x) + " = ", answer)
    
def asine_x(x):
    answer = math.asin(x)
    print("Arc sine of " + str(x) + " = ", answer)
    
def atan_x(x):
    answer = math.atan(x)
    print("Arc tan of " + str(x) + " = ", answer)
    
while True:  
    print("BASIC ARITHMETIC: \n A - Addition \n B - Substract \n C - Multiply \n D-  Divide \n E-  ADVANCE ARITHMETIC \n F-  Exit " )
    operation = input("Which operation do you want to perform? : ")

    if operation.upper() == "A":
        user_input_a = input("Enter first number: ")
        user_input_b = input("Enter second number: ")
        try:
            a = int(user_input_a)
            b = int(user_input_b)
            add(a, b)
        except ValueError:
            try:
                a = float(user_input_a)
                b = float(user_input_b)
                add(a, b)
            except ValueError:
                print("Invalid Input")
        
    elif operation.upper() == "B":
        user_input_a = input("Enter first number: ")
        user_input_b = input("Enter second number: ")
        try:
            a = int(user_input_a)
            b = int(user_input_b)
            substract(a, b)
        except ValueError:
            try:
                a = float(user_input_a)
                b = float(user_input_b)
                substract(a, b)
            except ValueError:
                print("Invalid Input")
        
    elif operation.upper() == "C":
        user_input_a = input("Enter first number: ")
        user_input_b = input("Enter second number: ")
        try:
            a = int(user_input_a)
            b = int(user_input_b)
            multiply(a, b)
        except ValueError:
            try:
                a = float(user_input_a)
                b = float(user_input_b)
                multiply(a, b)
            except ValueError:
                print("Invalid Input")
        
    elif operation.upper() == "D":
        user_input_a = input("Enter first number: ")
        user_input_b = input("Enter second number: ")
        try:
            a = int(user_input_a)
            b = int(user_input_b)
            divide(a, b)
        except ValueError:
            try:
                a = float(user_input_a)
                b = float(user_input_b)
                divide(a, b)
            except ValueError:
                print("Invalid Input")
        

    elif operation.upper() == "E":
        
        print(" POWER AND LOGARITHMIC FUNCTION \n a - x**y \n"
              " b - square root of x \n"
              " c - cube root of x \n "
              "d - logx \n"
              " e - exponent of x")
        
        print("TRIGONOMETRY FUNCTION \n"
              "f - cosine of x \n"
              "g - sine of x \n"
              "h - tan of x\n "
              "i - arc cosine of x \n"
              "j - arc sine of x \n"
              "k - arc tan of x")
        
        response = input("Which operation do you want to perform?\n ")
        
        if response.lower() == "a":
            user_input_x = input("Enter value for x \n ")
            user_input_y = input("Enter value for y \n ")
            try:
                x = int(user_input_x)
                y = int(user_input_y)
                power(x, y)
            except ValueError:
                try:
                    x = float(user_input_x)
                    y = float(user_input_y)
                    power(x, y)
                except ValueError:
                    print("Invalid Input")
            
        
        elif response.lower() == "b":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                square_root(x)
            except ValueError:
                try:
                    y = float(user_input)
                    square_root(y)
                except ValueError:
                    print("Invalid Input")
            
            
        elif response.lower() == "c":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                cube_root(x)
            except ValueError:
                try:
                    y = float(user_input)
                    cube_root(y)
                except ValueError:
                    print("Invalid Input")
            
            
        elif response.lower() == "d":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                log_x(x)
            except ValueError:
                try:
                    y = float(user_input)
                    log_x(y)
                except ValueError:
                    print("Invalid Input")
            
        elif response.lower() == "e":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                exponent_x(x)
            except ValueError:
                try:
                    y = float(user_input)
                    exponent_x(y)
                except ValueError:
                    print("Invalid Input")
            
            
        elif response.lower() == "f":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                cosine_x(x)
            except ValueError:
                try:
                    y = float(user_input)
                    cosine_x(y)
                except ValueError:
                    print("Invalid Input")
                    
        elif response.lower() == "g":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                sine_x(x)
            except ValueError:
                try:
                    y = float(user_input)
                    sine_x(y)
                except ValueError:
                    print("Invalid Input")
                      
            
        elif response.lower() == "h":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                tan_x(x)
            except ValueError:
                try:
                    y = float(user_input)
                    tan_x(y)
                except ValueError:
                    print("Invalid Input")
                    
        elif response.lower() == "i":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                acosine_x(x)
            except ValueError:
                try:
                    y = float(user_input)
                    acosine_x(y)
                except ValueError:
                    print("Invalid Input")

        elif response.lower() == "j":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                asine_x(x)
            except ValueError:
                try:
                    y = float(user_input)
                    asine_x(y)
                except ValueError:
                    print("Invalid Input")
        
        elif response.lower() == "k":
            user_input = input("Enter number: ")
            try:
                x = int(user_input) 
                atan_x(x)
            except ValueError:
                try:
                    y = float(user_input)
                    atan_x(y)
                except ValueError:
                    print("Invalid Input")
            
        else:
            print("Operation not supported")
            
    elif operation.upper() == "F":
        sys.exit()
    else:
        print("Operation not supported")
