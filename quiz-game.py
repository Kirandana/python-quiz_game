print("Welcome to my quiz!")
print("NOTE: Type your answers in all lowercase.")

question = input("Do you want to play? ")
if question != "yes":
    quit()

if question == "yes":
    print("Okay, let's play!")

    # Quiz Starts Here

questionOne = input("What does CPU stand for? ")
if questionOne != "central processing unit":
    print("Incorrect!")

if questionOne == "central processing unit":
    print("Correct, you got one point!")

questionTwo = input("What does CSS stand for? ")
if questionTwo != "cascading stylesheet":
    print("Incorrect!")

if questionTwo == "cascading stylesheet":
    print("Correct!")

questionThree = input("What does HTML stand for? ")
if questionThree != "hypertext markup language":
    print("Incorrect!")

if questionThree == "hypertext markup language":
    print("Correct!")

questionFour = input("What does JS stand for? ")
if questionFour != "javascript":
    print("Incorrect!")

if questionFour == "javascript":
    print("Correct!")
