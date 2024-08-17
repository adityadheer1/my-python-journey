#Sum of Even number to the Nth number
n = int(input("Enter n: "))
total = 0
number = range(0, (n + 1), 2)
for num in number:
    total += num

print(total)