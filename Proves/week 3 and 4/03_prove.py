child_meal_cost = float(input("What is the price of a child's meal? "))
adult_meal_cost = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adult = int(input("How many adults are there? "))
tax_rate = int(input("What is the sales tax rate? "))
print("\n")
total_child_cost = child_meal_cost * num_children
total_adult_cost = adult_meal_cost * num_adult

subtotal = total_adult_cost + total_child_cost
tax = (tax_rate * subtotal) / 100

total = subtotal + tax

print(f"Subtotal: ${total:.2f}")
print(f"Sales Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}\n")

payment_amount = float(input("what is the payment amount? $"))
change = payment_amount - total

if change < 0:
    print("Sorry that does not cover the bill please add more to the payment amount ")
elif change == 0:
    print("There is no change that is the exact amount ")
else:
    print(f"Change: ${change:.2f}")