people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 1000
youngest_name = ''
oldest = 0
oldest_name =''

for person in people:
    part = person.split()
    name = part[0]
    age = int(part[1])
    
    if age < youngest:
        youngest = age
        youngest_name = name
    elif age > oldest:
        oldest = age
        oldest_name = name
print(f"the youngest is {youngest_name} and their age is {youngest}")
print (f"the oldest is {oldest_name} and their age is {oldest}")