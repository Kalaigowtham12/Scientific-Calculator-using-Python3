import math

def scientific_calc (Input):
    if Input == 1:
        x = int(input("Enter first number : "))
        y = int(input("Enter another number: "))
        addition = x + y
        print("The addition of ", x, "and ", y, "is : ", addition)
    elif Input == 2:
        x = int(input("Enter first number : "))
        y = int(input("Enter another number: "))
        subtraction = x - y
        print("The subtraction of ", x, "and ", y, "is : ", subtraction)
    elif Input == 3:
        x = int(input("Enter first number : "))
        y = int(input("Enter another number: "))
        product = x * y
        print("The product of ", x, "and ", y, "is : ", product)
    elif Input == 4:
        x = int(input("Enter first number : "))
        y = int(input("Enter another number: "))
        division = x / y
        print("The division of ", x, "and ", y, "is : ", division)
    elif Input == 5:
        x = int(input("Enter a number : "))
        sin = math.sin(x)
        print("Sin value of ", x, "is : ", sin)
    elif Input == 6:
        x = int(input("Enter a number : "))
        cos = math.cos(x)
        print("Cos value of ", x, "is : ", cos)
    elif Input == 7:
        x = int(input("Enter a number : "))
        tan = math.tan(x)
        print("Tan value of ", x, "is : ", tan)
    elif Input == 8:
        x = int(input("Enter a number : "))
        log = math.log(x)
        print("Logarithmic value of ", x, "is : ", log)
    elif Input == 9:
        x = int(input("Enter a number : "))
        square_root = math.sqrt(x)
        print("The square root value of ", x, "is : ", square_root)
    elif Input == 10:
        x = int(input("Enter a number : "))
        factorial = math.factorial(x)
        print("The factorial value of ", x, "is : ", factorial)
    else:
        print("Enter a valid option please")


print('''
 Press : 
   1. Addition
   2. Subtraction
   3. Multiplication
   4. Division
   5. Sin
   6. cos
   7. tan
   8. log
   9. Square root
   10. Factorial
   ''')

Input = int(input("Enter option: "))
scientific_calc(Input)