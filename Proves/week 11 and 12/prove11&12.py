play = ""
while play == "":
    with open("life-expectancy.csv") as file:
        #skips the first line and gets to the numbers
        next(file)
        #the large totals for the data set
        lowest = 100.00
        highest = 0.00
        total = 0.00
        i = 0
        # used for the user inputs to the program
        newPage = "\n\n\n\n\n\n\n\n\n"
        userYear = int(input(f"what year do you want to see life expectancy for? (valid inputs 1751 to 2019) "))
        lowestUserExpectancy = 100.00
        highestUserExpectancy = 0.00
        lowestUserCountry = ''
        highestUserCountryName = ''
        if userYear < 2020 and userYear > 1750:
            for line in file:
                part = line.split(",")
                countryName = part[0]
                countryCode = part[1]
                countryYear = int(part[2])
                lifeExpectancy = float(part[3])
                if lowest > lifeExpectancy:
                    lowest = lifeExpectancy
                    lowestCountryName = countryName
                    lowestCountryYear = countryYear
                elif highest < lifeExpectancy:
                    highest = lifeExpectancy
                    highestCountryName = countryName
                    highestCountryYear = countryYear
                elif userYear == countryYear:
                    i += 1
                    total += lifeExpectancy
                    print(f"{countryName} in {countryYear} had life expectancy of {lifeExpectancy} years")
                    if highestUserExpectancy < lifeExpectancy:
                        highestUserExpectancy = lifeExpectancy
                        highestUserCountryName = countryName
                    elif lowestUserExpectancy > lifeExpectancy:
                        lowestUserExpectancy = lifeExpectancy
                        lowestUserCountry = countryName
               


                    
            print (f"\n\n-----In {userYear} the overall life expectancy was {total/i:.3f} years-----") 
            print(f"The lowest life expectancy rate this year is in {lowestUserCountry} with {lowestUserExpectancy}")
            print(f"The highest life expectancy rate this year is in {highestUserCountryName} with {highestUserExpectancy}")
            play = input("press enter to look up another year or type 'q' to quit: ")
        else: 
            print(f"{newPage}Invalid option. Please enter a year between 1751 - 2019: ")
print (f"{newPage}Goodbye, Here are the total life expectancy lowest and highest ")       
print (f"\nthe lowest life expectancy total is in {lowestCountryName} in {lowestCountryYear} with a life expectancy of {lowest} years")
print (f"the highest life expectancy total is in {highestCountryName} in {highestCountryYear} with a life expectancy of {highest} years\n\n")

