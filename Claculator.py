import time
import sys


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)


def delay_print2(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2)


delay_print("Select operation.\n")
delay_print("1.Add\n")
delay_print("2.Subtract\n")
delay_print("3.Multiply\n")
delay_print("4.Divide\n")

calc = True

while calc:

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        delay_print2("Invalid Input\n")

    con: str = input("Continue? (y/n): ")
    print()

    if con == "n":
        calc = False
    elif con == "y":
        calc = True
    else:
        delay_print2("Invalid Input!\nClosing...")
        delay_print2("Closing...")
        delay_print2("Closed!")
        calc = False
