# Function to calculate how much each person should pay
# when splitting a bill, including tip

def calculate_tip(total, tip_percent, num_people):
    tip_amount = total * (tip_percent / 100)
    total_with_tip = total + tip_amount
    per_person = total_with_tip / num_people
    return round(per_person, 2)

# Example usage
bill = float(input("Enter the bill amount: "))
tip = int(input("Enter tip percentage: "))
people = int(input("How many people? "))

amount = calculate_tip(bill, tip, people)
print(f"Each person should pay: ${amount}")
