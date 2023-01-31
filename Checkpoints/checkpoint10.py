print("Please enter the items of the shopping list (type: quit to finish):")

ListOfItems = []
item = None

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        ListOfItems.append(item)

print("\nThe shopping list is:")
for item in ListOfItems:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(ListOfItems)):
    item = ListOfItems[i]
    print(f"{i}. {item}")

print()
i = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

ListOfItems[i] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(ListOfItems)):
    item = ListOfItems[i]
    print(f"{i}. {item}")