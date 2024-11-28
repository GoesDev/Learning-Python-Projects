number = input("Enter a number: ")

try:
    x = 10 / int(number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only numbers")
else:
    print(x)
