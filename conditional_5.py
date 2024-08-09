#Lets suggest you what activity you can consider based on the weather.

weather = input("How the weather outside? It is Sunny?, Rainy? or Snowing?").lower()

if weather == "sunny":
    print("Heard that it is sunny outide, You might consider taking a walk")
elif weather == "rainy":
    print("Damnit, its raining outside, lets brew a coffee and read some books")
else:
    print("Its that month of the year where we build a snowman!!")