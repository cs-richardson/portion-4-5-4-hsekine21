# 4.4.5 Presidential Eligibility
# Program that checks if user is over 35 years old, born in the US, and has been
# a resident for at least 14 years and tells them if they are eligible for
# presidency

# Hina Sekine

age = input("Age: ")
while not(age.isdigit()):
    age = input("Age: ")

citizen = input("Born in the U.S.? (y / n): ")
while citizen != 'y' and citizen != 'n':
    citizen = input("Born in the U.S.? (y / n): ")

yearsLivedUsa = input("Years of Residency?: ")
while not(yearsLivedUsa.isdigit()):
    yearsLivedUsa = input("Years of Residency?: ")

if int(age) >= 35 and citizen == 'y' and int(yearsLivedUsa) >= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president") 
