#Choose a mode of transportation based on distance

dist = int(input("How far is your destination? : "))

if dist <= 3:
    print("You should prefer walking up there")
elif dist <=15:
    print("You should prefer riding a bike up there")
else:
    print("You should take your car")