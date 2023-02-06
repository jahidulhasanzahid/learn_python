# logical operator (and, or, not) = used to check if two or more conditional statement is ture
# not operator work like reverse. it's make ture statement to fasle , and false to true

temp = int(input("What is the Temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("You can go outside!")
elif temp < 0 or temp > 30:
    print("The Temperature is bad today")
    print("Stay home")
else:
    print("Somethign wrong!")