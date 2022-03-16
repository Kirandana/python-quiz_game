print("Welcome to my quiz!")
print("NOTE: Type your answers in all lowercase.")

question = input("Do you want to play? ")
if question != "yes":
    quit()

if question == "yes":
    print("Okay, let's play!")

cpu = input("What does CPU stand for? ")
if cpu != "central processing unit":
    print("Incorrect!")

if cpu == "central processing unit":
    print("Correct, you got one point!")
