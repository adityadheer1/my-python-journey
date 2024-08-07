#Grade Calculator
marks = int(input("Enter your grades to check: "))

if marks >=90:
    grade = "A"
    print(f'Congratulations, you have got {grade}.')
elif marks >= 80:
    grade = "B" 
    print(f'Congratulations, you have got {grade}.')
elif marks >= 70:
    grade = "C" 
    print(f'Congratulations, you have got {grade}.')
elif marks >= 60:
    grade = "D" 
    print(f'Congratulations, you have got {grade}.')
else:
    grade = "F"
    print(f"You got {grade}, Need to work hard.")