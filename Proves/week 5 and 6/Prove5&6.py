
#land scenario
print("Welcome to the text based adventure! \n")
start_position =input("Do you want to start out on LAND or on WATER? ").lower()

#I decided to add a scenario for land and water I didn't spend as much time on water just because the options got a bit tedious but adding them as functions was a fun expermiment 

def LandScenario():
    #choice number 1 shelter, food or smoke
    landChoiceOne = input("\nYou chose land. \n\nYou find yourself on a strange island. \nThere is smoke in the distance what do you do first? \ncreate a SHELTER, find FOOD or head towards the SMOKE?").lower()
    if landChoiceOne == "shelter":
        shelter = input("'\n\nYou chose shelter. You find some timber nearby and build a modest Nacho Libre shelter. \nYou notice there seem to be some scuffles around you.\nWhat do you do next? light a FIRE to see or go to SLEEP?").lower()
        if shelter =="fire":
            print("you light a fire but this draws attention from a group of traders nearby. They kill you. \n\n----GAME OVER----")
            quit()
        elif shelter == "sleep":
            print("You never wake up \n\n----GAME OVER----")
            quit()
    elif landChoiceOne == "food":
        print("\nYou chose food. \n\nYou find some dead fish to eat. \nYou eat them raw and don't feel too good. \nYou actually die later that night from the horrible fish \n\n----GAME OVER----")
        quit()
    elif landChoiceOne == "smoke":
        smoke = input("\nYou chose smoke. \n\nYou make the day long journey to the smoke and come across a group of savages. \nThey want you to either JOIN or FIGHT another castaway they found to the death. \nWhat do you choose?").lower()
        if smoke == "join":
            leader = input("Congrats you join them and rise through the ranks to their leader. \n Do you STAY on the island or do you ESCAPE? \n").lower()
            if leader == "stay":
                print("Congratulations you win!")
                quit()
            elif leader == "escape":
                print("your crew rebels against you \n\n----GAME OVER----")
        elif smoke == "fight":   
            print("You die in the 1V1 battle \n\n----GAME OVER----")
    #water Scenario




def WaterScenario():
    waterChoiceOne = input("\nYou chose water. \n\nYou wake up and find yourself on a small raft out at sea. \nNothing but water in sight what do you do first? \nOpen the mysterious CHEST, look at the scuffed up MAP\n").lower()
    if waterChoiceOne == "chest":
        print("\n\nit is booby trapped and you do not survive. \n\n----GAME OVER----")
        quit()
    elif waterChoiceOne == "map":
        map = input("\nYou chose map. \nDo you seek out the red X on the map or do you head towards the LAND? \n\n").lower()
        if map == "x":
            x = input("\nYou chose red X. \nyou find a ton of treasure under the water in a sunken ship. \nDo you LOAD the treasure on the raft or take the inflatable LIFEBOAT?\n").lower()
            if x == "load":
                print("You make it some distance before your raft sinks. \nYou stay afloat a few hours longer but alas \n\n----GAME OVER----")
                quit()
            elif x == "lifeboat":
                print("you leave the treasure behind but save your life! congratulations you survive and WIN!!!")
                quit()
        elif map == "land":
            print("You head towards land and you survive! you win!!!")
            quit()




while(start_position!= "exit"):
    if start_position == "land":
        LandScenario()
    elif start_position =="water":
        WaterScenario()
    else:
        print("\nSorry that is not a valid input. your inputs are either LAND or WATER please try again")
        start_position =input("Do you want to start out on LAND or on WATER? ").lower()