# Print Multiplication table of any given number
n = int(input("Enter the number: "))

for num in range(1, 11):
    if num == 5:
        # print("Skip this iteration" ) 
        #solution by HC
        continue #this will skip the iteration
    outcome = num * n
    print(f"{num} * {n} = {outcome}")