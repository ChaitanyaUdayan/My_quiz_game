print( """Welcome to my Game. 
Enjoy game and use Only Small Letter's while answering and no special Characters.""" )

playing = input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()
print("Okay! Let's play (: ")

question = input("What does the CPU Stands for? ")
if question ==("central processing unit"):
    print("Correct!, Well Played")
else:
    print("Incorrect!, Try again.")

question = input("What does the OOPS Stands for? ")
if question ==("object oriented programming system"):
    print("Correct!, Well Played")
else:
    print("Incorrect!, Try again.")

question = input("What does the SQL Stands for? ")
if question ==("Structured Query Language"):
    print("Correct!, Well Played")
else:
    print("Incorrect!, Try again.")

question = input("What does the AIC Stands for? ")
if question ==("ampere interrupting capacity"):
    print("Correct!, Well Played")
else:
    print("Incorrect!, Try again.")

question = input("What does the mA Stands for? ")
if question ==("milliampere"):
    print("Correct!, Well Played")
else:
    print("Incorrect!, Try again.") 