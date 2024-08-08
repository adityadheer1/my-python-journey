#Determine if the Fruit is ripe, overripe or unripe, based on its color
color = input("Let us know whats the color: green, yellow or brown: ").lower()

if color == "yellow":
    print("Banana is ripped")
elif color == "brown":
    print("Banana is overripped")
else:
    print("Banana is unripe")