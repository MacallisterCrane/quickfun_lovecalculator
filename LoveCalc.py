print("Welcome to the love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

#Random calculation here for compatability
combined_name = name1 + name2
lower_case = combined_name.lower()
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

true = t + r + u + e
love = l + o + v + e

final = int(str(true) + str(love))
if final < 10 or final > 90:
        print(f"Your score is {final}, you go together like coke and mentos.")
elif final >= 40 and final <= 50:
        print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}")
