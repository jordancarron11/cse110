word = "Commitment"
word = word.lower()
favoriteLetter = input("what is your favorite letter? ")
for i, letter in enumerate(word):
    if letter == "m":
        print (letter.upper(), end="")
    elif letter == favoriteLetter:
        letter = '_'
        print (letter,end='')
    else:
        print(letter, end="")
print("\n\n")
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
nth = int(input("how many letters until it capitolizes again? "))
run = "yes"
while run == "yes":
    for n, letter in enumerate(quote):
        if n % nth == 0:
            print(letter.upper(),end='')
        else:
            print(letter, end='')
    run = input("\n\nwant to run again? (yes/no) ")