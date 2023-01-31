print("\nWelcome to the shopping cart program!")
#prints menu choices 
NewPage = '\n\n\n\n\n\n\n\n\n\n\n\n'
items = []
costs = []
itemAndCost = []
def  Menu():
    print("\nPlease choose from the following options:\n1. Add Item\n2. Display Items\n3. Remove Item\n4. Calculate total\n5. Quit")
#adds new items 
def Add():
    addItem = input(f"{NewPage}What item do you want to add? ")
    addCost = float(input("\nHow much does it cost? $"))
    items.append(addItem)
    costs.append(addCost) 
    addItemWCost = (f'Item: {addItem} Cost ${addCost:.2f}')
    itemAndCost.append(addItemWCost)
#displays the list of item
def Display():
    for item in itemAndCost:
        print (f"    {item}")
#displays list of items and then gives the option for user to remove them based on number
def Remove():
    remove = 'play'
    while remove != 'quit':
        num = 1
        for item in itemAndCost:
            print (f"{num}. {item}")
            num +=1
        pickItem = int(input("Type the number of the item you want to remove or press 0 to quit "))
        if pickItem >= len(itemAndCost) and pickItem != 0:
            del(itemAndCost[pickItem-1])
        elif pickItem == 0:
            remove = "quit"
        else:
            print(f"{NewPage}Sorry that is not a valid imput \n")
          
userChoice =''
while userChoice != '5' or 'quit':
    Menu()
    userChoice = input("What number do you chose? ").lower()
    if userChoice == '1' or userChoice == 'add':
        Add()
    elif userChoice == '2' or userChoice == 'display':
        print("\n\n\n----- Items In Your Lists -----")
        Display()
    elif userChoice == '3' or userChoice == 'remove':
        Remove()
    elif userChoice == '5' or userChoice == 'quit':
        print("Goodbye!")
        quit()
    else:
        print("\n\nSorry that is an invalid option. ")

