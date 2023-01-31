friends = []
play = 'yes'
num = 1


addFriend = ''
play = 'yes'
while play == 'yes':
    if addFriend == "":
        nameOfFriend = input(f"What is your {num} friends name? ")
        num +=1
        if nameOfFriend != 'end':
            friends.append(nameOfFriend)
            addFriend = input("to add another friend press enter type anything to exit: ")
        else:
            play = 'no'

    else:
        play = 'no'
print("\nyour friends are:")
for friend in friends:
    print(friend)
