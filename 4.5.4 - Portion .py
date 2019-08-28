# 4.5.4 - Portion
# Modification so that the compared floats are compared as rounded integers 
# Hina Sekine 

# Amount of food and number of people
tons_of_food = 0.07
num_people = 25

# Determine how much food each person gets
tons_of_food_per_person = tons_of_food / num_people
print(tons_of_food_per_person)

# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take?: "))

# changed to have 5 floating points
tons_taken = round(tons_taken, 5)
tons_of_food_per_person = round(tons_of_food_per_person, 5)

if tons_taken == tons_of_food_per_person: 
    print("Good job, you took the right amount of food!")
else:
    print("You took the wrong amount of food!")
