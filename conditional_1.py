#Age Group Categorization. Child <13, 13-19 teenager, 20-59 Adult and 60+ senior

your_age = int(input('Enter your age to check your age group: '))

if your_age < 13:
    print("Child")
elif your_age <= 19:
    print("Teen")
elif your_age >= 20 and your_age <= 59:
    print("adult")
else:
    print("Senior")