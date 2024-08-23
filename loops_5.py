#Identify the first non repeated character in a String
word = "teeteraassdd"

for char in word:
    if word.count(char) == 1:
        print("char is:", char)
        break # break will dicontinue the loop once if condition is met.
    
    