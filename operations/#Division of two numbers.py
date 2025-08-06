# Division of two numbers

num1 = float(input("Enter numerator: "))
num2 = float(input("Enter denominator: "))


if num2 == 0:
    print("Error: Cannot divide by zero.")
else:
    result = num1 / num2
    print("The division of", num1, "by", num2, "is:", result)
