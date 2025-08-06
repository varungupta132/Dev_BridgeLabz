from operations.addition import add
from operations.subtraction import subtract
from operations.multiplication import multiply
from operations.division import divide

def main():
    print("=== Calculator App ===")
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            if b != 0:
                print("Result:", divide(a, b))
            else:
                print("Error: Cannot divide by zero.")
    else:
        print("Invalid input. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
