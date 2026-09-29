# ==========================================
# YVETTE MENSAH NSAFOAH
# GKS PORTFOLIO - SMART CALCULATOR
# ==========================================

import math


def show_menu():
    print("\n" + "=" * 45)
    print("        YVETTE'S SMART CALCULATOR")
    print("=" * 45)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. View Calculation History")
    print("9. Exit")
    print("=" * 45)


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("❌ Please enter a valid number.")


def addition():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    result = a + b
    print(f"✅ Result: {result}")
    return f"{a} + {b} = {result}"


def subtraction():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    result = a - b
    print(f"✅ Result: {result}")
    return f"{a} - {b} = {result}"


def multiplication():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    result = a * b
    print(f"✅ Result: {result}")
    return f"{a} × {b} = {result}"


def division():
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if b == 0:
        print("❌ You cannot divide by zero.")
        return None

    result = a / b
    print(f"✅ Result: {result}")
    return f"{a} ÷ {b} = {result}"


def power():
    a = get_number("Enter the base: ")
    b = get_number("Enter the exponent: ")
    result = a ** b
    print(f"✅ Result: {result}")
    return f"{a}^{b} = {result}"


def square_root():
    a = get_number("Enter a number: ")

    if a < 0:
        print("❌ Cannot calculate the square root of a negative number.")
        return None

    result = math.sqrt(a)
    print(f"✅ Result: {result}")
    return f"√{a} = {result}"


def percentage():
    number = get_number("Enter the number: ")
    percent = get_number("Enter the percentage: ")

    result = (percent / 100) * number

    print(f"✅ {percent}% of {number} = {result}")
    return f"{percent}% of {number} = {result}"


def show_history(history):
    print("\n" + "=" * 45)
    print("          CALCULATION HISTORY")
    print("=" * 45)

    if not history:
        print("No calculations yet.")
    else:
        for number, calculation in enumerate(history, start=1):
            print(f"{number}. {calculation}")

    print("=" * 45)


def main():
    history = []

    print("\n👋 Welcome to Yvette's Smart Calculator!")

    while True:
        show_menu()

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            calculation = addition()

        elif choice == "2":
            calculation = subtraction()

        elif choice == "3":
            calculation = multiplication()

        elif choice == "4":
            calculation = division()

        elif choice == "5":
            calculation = power()

        elif choice == "6":
            calculation = square_root()

        elif choice == "7":
            calculation = percentage()

        elif choice == "8":
            show_history(history)
            continue

        elif choice == "9":
            print("\n👋 Thanks for using Yvette's Smart Calculator!")
            print("Good luck with your GKS journey! 🇬🇭 → 🇰🇷")
            break

        else:
            print("❌ Invalid choice. Please choose 1-9.")
            continue

        if calculation is not None:
            history.append(calculation)


if __name__ == "__main__":
    main()
    