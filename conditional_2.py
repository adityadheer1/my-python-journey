#Movie Ticket pricing
age = int(input("Enter your age:"))
day = input("Enter today's day(s, m, t, w, th, f, sa): ")

tkt_price = 0

if age < 18 :
    tkt_price = 8
else:
    tkt_price = 12
#Solution by HC.
tkt_price = 12 if age >= 18 else 8 #short and Crisp code.

dis_tkt = 0
if day == "w":
    dis_tkt = tkt_price - 2
    print(f"Please play ${dis_tkt}")
else:
    print(f"Please play ${tkt_price}")