def safe_divide(a, b):
    try:
        result = a / b
        return round(result, 2)
    except ZeroDivisionError:
        return "❌ Cannot divide by zero."
    except TypeError:
        return "❌ Invalid input type."

while True:
    try:
        x = float(input("Enter numerator: "))
        y = float(input("Enter denominator: "))
        print("Result:", safe_divide(x, y))
    except ValueError:
        print("⚠️ Please enter valid numbers.")
    
    again = input("Try again? (y/n): ").lower()
    if again != "y":
        print("👋 Goodbye!")
        break
