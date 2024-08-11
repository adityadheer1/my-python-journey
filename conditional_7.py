#Lets help you customizing your coffee
size = input("Which size due you prefer your coffee? : Small, Medium or Large?").lower()
add_on = input("Would you like to have an extra Espresso? ").lower()

cup = ""
if size == "small":
    cup = "Small"
elif size == "medium":
    cup = "Medium"
else:
    cup = "Large"

espresso = ""
if add_on == "yes" or add_on == "y":
    espresso = "an extra"
else:
    espresso = "No"

print(f"Here is your {cup} coffee with {espresso} Espresso shot")