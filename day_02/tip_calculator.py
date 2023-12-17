greeting = "Welcome to the tip calculator."
print(greeting)

total_bill = float(input("What was the total bill? $"))
percent_tip = float(input("What percentage tip would you like to givr? 10, 12, or 15? ")) / 100
num_people = int(input("How many people to split the bill? "))

total_bill_plus_tip = total_bill * (1 + percent_tip)
total_per_person = round(total_bill_plus_tip / num_people, 2)

print(f"Each person should pay: $", total_per_person)
