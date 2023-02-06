# if else statement = a block of code that will execute if it's condition is true

mark = int(input("what is your Math Mark? "))

if mark == 100:
    print("WOW! You got full mark. You are awesome! It's A+")
elif mark >= 80:
    print("You got A+ Grade!")
elif mark >= 70:
    print("You got A Grade")
elif mark < 33:
    print("You Failed!")
else:
    print("Your result is not published Yet!")
